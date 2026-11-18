#!/usr/bin/env python3
"""Execute the proved relative periodic fan resolution, retaining every lattice map.

The three sector lattices have order (Z,V,base0,base1).  This program
does not assign an analytic quotient, a fixed-stratum topology, or a return.
"""
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations
from collections import defaultdict
from functools import lru_cache, reduce
from math import gcd
import argparse
import heapq
import json
import time

ROOT = Path(__file__).resolve().parents[2]
I = ((1, 0), (0, 1))
SECTORS = ("I", "W", "E")


def primitive(v):
    g = reduce(gcd, (abs(x) for x in v))
    assert g > 0
    return tuple(x // g for x in v)


def det3(A):
    (a,b,c),(d,e,f),(g,h,i) = A
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


@lru_cache(maxsize=200000)
def det4(C):
    A = tuple(zip(*C))
    return sum((-1)**j*A[0][j]*det3(tuple(tuple(A[i][k] for k in range(4) if k != j) for i in range(1,4))) for j in range(4))


def matvec(P, n):
    return (P[0][0]*n[0]+P[0][1]*n[1], P[1][0]*n[0]+P[1][1]*n[1])


class PeriodicFan:
    def __init__(self, a, b, N):
        self.a, self.b, self.N = a, b, N
        self.P = {"I": I, "W": ((1,b),(-a,-2)), "E": ((0,0),(0,N))}
        self.H = ((2,b),(-a,N-1))
        self.checks = 0
        self.cells = {}
        self.by_key = {}
        self.face_index = defaultdict(set)
        self.heap = []
        self.next_id = 0
        self.trace = []
        self.initial_counts = {}
        self.protected = {}
        self.started = time.monotonic()

    def ck(self, value, label):
        assert value, label
        self.checks += 1

    def T(self, sector, v, n):
        x,y,r,s = v
        P,H = self.P[sector], self.H
        return (x+(r*P[0][0]+s*H[0][0])*n[0]+(r*P[0][1]+s*H[0][1])*n[1],
                y+(r*P[1][0]+s*H[1][0])*n[0]+(r*P[1][1]+s*H[1][1])*n[1],r,s)

    def canonical(self, sector, C):
        X,Y,R,S = map(sum, zip(*C))
        P,H = self.P[sector], self.H
        if S or sector == "I":
            aa,bb = R*P[0][0]+S*H[0][0], R*P[0][1]+S*H[0][1]
            cc,dd = R*P[1][0]+S*H[1][0], R*P[1][1]+S*H[1][1]
            determinant = aa*dd-bb*cc
            assert determinant > 0
            n = ((dd*X-bb*Y)//determinant, (aa*Y-cc*X)//determinant)
        elif sector == "W":
            assert R > 0 and Y == -self.a*X
            n = (X//R, 0)
        else:
            assert R > 0 and X == 0
            n = (0, Y//(R*self.N))
        C0 = tuple(sorted(self.T(sector,v,(-n[0],-n[1])) for v in C))
        return C0, n

    def face_key(self, sector, C):
        C0,n = self.canonical(sector,C)
        tag = "H" if all(v[2] == 0 for v in C) else sector
        return (tag,len(C),C0),n

    def ray(self, P, n, height):
        return (*matvec(P,n),1-height,height)

    def initial(self):
        fans = {}
        for sector in SECTORS:
            u,v = ((1,0),(-self.b,1)) if sector == "W" else ((1,0),(0,-1))
            uv = (u[0]+v[0],u[1]+v[1])
            Cset = set()
            for w in (u,v):
                ns = ((0,0),w,uv)
                lo = [self.ray(self.P[sector],n,0) for n in ns]
                hi = [self.ray(self.H,n,1) for n in ns]
                for C in ((lo[0],lo[1],lo[2],hi[2]),(lo[0],lo[1],hi[1],hi[2]),(lo[0],hi[0],hi[1],hi[2])):
                    if det4(tuple(C)):
                        Cset.add(self.canonical(sector,C)[0])
            fans[sector] = Cset
        self.initial_counts['raw'] = {s:len(fans[s]) for s in SECTORS}

        # The exact common-H overlay has a single new midpoint orbit for b=2.
        # Its original integral primitive ray is (2,N-1,0,2), not a height-one
        # rational point.  Each old triangle has at most one edge in this orbit.
        if self.b == 2:
            p = primitive((self.b,self.N-1,0,2))
            for sector in SECTORS:
                ns = ((1,0),(-1,1)) if sector == "W" else ((0,0),(0,1))
                F = tuple(self.ray(self.H,n,1) for n in ns)
                Fc,n0 = self.canonical(sector,F)
                pc = self.T(sector,p,(-n0[0],-n0[1]))
                new = set()
                for C in fans[sector]:
                    matches = []
                    for inds in combinations(range(4),2):
                        FF = tuple(C[i] for i in inds)
                        if any(v[2] for v in FF):
                            continue
                        FFc,n = self.canonical(sector,FF)
                        if FFc == Fc:
                            matches.append((inds,n))
                    self.ck(len(matches)<=1,'H edge orbit separation')
                    if not matches:
                        new.add(C)
                    else:
                        inds,n = matches[0]
                        pp = self.T(sector,pc,n)
                        self.ck(primitive(pp)==pp,'H overlay primitive ray')
                        for i in inds:
                            D = list(C);D[i] = pp
                            self.ck(det4(tuple(D)) != 0,'H overlay nonzero star cone')
                            new.add(self.canonical(sector,D)[0])
                fans[sector] = new

        # The actual E filling prescribes every primitive height-one chain ray.
        # Subdivide its raw length-N bottom edge and join with the unchanged
        # opposite face; this literal join leaves H and every period map fixed.
        new = set()
        for C in fans['E']:
            bottom = [i for i,v in enumerate(C) if v[3] == 0]
            if len(bottom) == 2:
                i,j = sorted(bottom,key=lambda k:C[k][1])
                lo,hi = C[i][1],C[j][1]
                self.ck(hi-lo == self.N,'raw E boundary interval length N')
                for k in range(lo,hi):
                    D = list(C);D[i]=(0,k,1,0);D[j]=(0,k+1,1,0)
                    self.ck(det4(tuple(D)) != 0,'E chain joined cone is nonzero')
                    new.add(self.canonical('E',D)[0])
            else:
                self.ck(len(bottom)==1,'E full cone has one or two bottom rays')
                new.add(C)
        fans['E'] = new
        self.initial_counts['prescribed_boundary_refinement'] = {s:len(fans[s]) for s in SECTORS}
        self.check_H(fans)
        for sector in SECTORS:
            self.protected[sector] = self.protected_faces(sector,fans[sector])

        # Relative barycentric separator: a protected face is left literally
        # unchanged.  Every other face uses the primitive sum of its own rays.
        @lru_cache(maxsize=None)
        def bary(F):
            if all(v[3] == 0 for v in F) or len(F)==1:
                return (F,)
            p = primitive(tuple(map(sum,zip(*F))))
            out = set()
            for i in range(len(F)):
                for Q in bary(F[:i]+F[i+1:]):
                    out.add(tuple(sorted((*Q,p))))
            return tuple(out)

        for sector in SECTORS:
            Cs = {self.canonical(sector,D)[0] for C in fans[sector] for D in bary(C)}
            self.initial_counts.setdefault('relative_separator',{})[sector]=len(Cs)
            for C in sorted(Cs):
                self.add(sector,C)
        self.check_H({s:{C for (ss,C) in self.by_key if ss==s} for s in SECTORS})
        for sector in SECTORS:
            self.ck(self.protected_faces(sector,[C for ss,C in self.by_key if ss==sector])==self.protected[sector], 'separator preserves '+sector+' boundary')

    def protected_faces(self,sector,cones):
        d = 3 if sector == 'I' else 2
        return {self.canonical(sector,tuple(C[i] for i in inds))[0]
                for C in cones for inds in combinations(range(4),d)
                if all(C[i][3] == 0 for i in inds)}

    def check_H(self,fans):
        sets=[]
        for sector in SECTORS:
            sets.append({self.canonical(sector,tuple(C[i] for i in inds))[0]
                         for C in fans[sector] for inds in combinations(range(4),3)
                         if all(C[i][2] == 0 for i in inds)})
        self.ck(sets[0]==sets[1]==sets[2],'all actual H boundary triangles agree')

    def separated(self,sector,C):
        keys = [self.canonical(sector,(v,))[0] for v in C if v[3]>0]
        self.ck(len(set(keys))==len(keys),'nonprotected ray orbit separation')

    def add(self,sector,C):
        C = self.canonical(sector,C)[0]
        key=(sector,C)
        if key in self.by_key:
            return self.by_key[key]
        D=abs(det4(C));self.ck(D>0,'maximal cone has rank four')
        self.separated(sector,C)
        cid=self.next_id;self.next_id+=1
        entries=[]
        for d in range(1,5):
            for inds in combinations(range(4),d):
                F=tuple(C[i] for i in inds);fk,n=self.face_key(sector,F)
                ent=(cid,inds,n)
                self.face_index[fk].add(ent);entries.append((fk,ent))
        self.cells[cid]={'sector':sector,'C':C,'D':D,'entries':entries}
        self.by_key[key]=cid;heapq.heappush(self.heap,(-D,cid))
        return cid

    def remove(self,cid):
        z=self.cells.pop(cid)
        del self.by_key[(z['sector'],z['C'])]
        for fk,ent in z['entries']:
            self.face_index[fk].remove(ent)
            if not self.face_index[fk]:del self.face_index[fk]

    def point(self,C):
        A=tuple(zip(*C));signed=det4(C);D=abs(signed);sgn=1 if signed>0 else -1
        for j in range(4):
            nums=[]
            for i in range(4):
                minor=tuple(tuple(A[r][k] for k in range(4) if k!=i) for r in range(4) if r!=j)
                nums.append((sgn*(-1)**(i+j)*det3(minor))%D)
            if any(nums):
                p=tuple(sum(C[i][r]*nums[i] for i in range(4))//D for r in range(4))
                self.ck(all(sum(C[i][r]*nums[i] for i in range(4))==D*p[r] for r in range(4)),'half-open point is exactly integral')
                g=reduce(gcd,(abs(x) for x in p));pp=tuple(x//g for x in p)
                self.ck(primitive(pp)==pp,'resolution point primitive')
                return pp,nums,D*g,j
        raise AssertionError('singular inverse has a nonintegral column')

    def resolve(self,progress=100):
        steps=0
        while self.heap:
            negD,cid=heapq.heappop(self.heap)
            if cid not in self.cells:continue
            if negD==-1:break
            z=self.cells[cid];sector,C,D=z['sector'],z['C'],z['D']
            p,nums,den,j=self.point(C)
            inds=tuple(i for i,n in enumerate(nums) if n)
            F=tuple(C[i] for i in inds);Fc,n0=self.canonical(sector,F)
            fk,_=self.face_key(sector,F)
            pc=self.T(sector,p,(-n0[0],-n0[1]))
            coeff={self.T(sector,C[i],(-n0[0],-n0[1])):nums[i] for i in inds}
            self.ck(len(inds)>=2 and pc[3]>0,'centre is a nonprotected higher-dimensional face')
            affected=list(self.face_index[fk])
            self.ck(len({e[0] for e in affected})==len(affected),'at most one translated centre in each cone')
            replacements=[];old=[]
            for aid,ais,an in affected:
                az=self.cells[aid];asec,AC,AD=az['sector'],az['C'],az['D']
                pp=self.T(asec,pc,an)
                children=[]
                for ai in ais:
                    cr=self.T(asec,AC[ai],(-an[0],-an[1]))
                    num=coeff[cr]
                    CC=list(AC);CC[ai]=pp;CC=self.canonical(asec,CC)[0]
                    DD=abs(det4(CC))
                    self.ck(0<DD<AD and DD*den==num*AD,'every incident determinant strictly drops')
                    children.append(DD);replacements.append((asec,CC))
                old.append({'cell':aid,'sector':asec,'determinant':AD,'period':an,'new_determinants':children})
            for aid,_,_ in affected:self.remove(aid)
            newids=[self.add(asec,CC) for asec,CC in replacements]
            self.trace.append({'step':steps,'selected_cell':cid,'selected_determinant':D,'face_sector':fk[0],
                               'face_rays':Fc,'ray':pc,'coefficient_denominator':den,
                               'coefficient_numerators':[coeff[v] for v in Fc],'inverse_column':j,
                               'affected':old,'new_cells':newids})
            steps+=1
            if progress and steps%progress==0:
                print(f'{self.a},{self.b},{self.N}: {steps} stars; {len(self.cells)} cone orbits; max selected determinant {D}; {time.monotonic()-self.started:.1f}s',flush=True)
        self.ck(all(z['D']==1 for z in self.cells.values()),'every final maximal cone is regular')
        fans={s:{C for ss,C in self.by_key if ss==s} for s in SECTORS}
        self.check_H(fans)
        for sector in SECTORS:
            self.ck(self.protected_faces(sector,fans[sector])==self.protected[sector], 'resolution preserves exact '+sector+' boundary')

    def export(self):
        # A ray occurrence has a literal vector as well as its canonical orbit
        # vector and recovered integral period.  No column is replaced by its
        # orbit representative inside a cone.
        ordered=sorted(self.cells.values(),key=lambda z:(z['sector'],z['C']))
        literal={s:{} for s in SECTORS};rayorbits={s:{} for s in SECTORS}
        def rid(sector,v):
            if v not in literal[sector]:literal[sector][v]=f'{sector}r{len(literal[sector])+1}'
            return literal[sector][v]
        def oid(sector,v):
            vc,n=self.canonical(sector,(v,));w=vc[0]
            if w not in rayorbits[sector]:rayorbits[sector][w]=f'{sector}o{len(rayorbits[sector])+1}'
            return rayorbits[sector][w],w,n
        cones=[];faceocc=defaultdict(list)
        for k,z in enumerate(ordered,1):
            sector=z['sector'];C=list(z['C'])
            if det4(tuple(C))<0:C[0],C[1]=C[1],C[0]
            self.ck(det4(tuple(C))==1,'exported ordered maximal cone determinant is +1')
            cid=f'{sector}c{k}'
            rays=[rid(sector,v) for v in C]
            cones.append({'id':cid,'sector':sector,'ordered_rays':rays,'determinant':1,
                          'orbit_representative':'floor of (R P0+S H)^(-1) times summed fibre coordinates',
                          'historical_cell_id':self.by_key[(sector,z['C'])]})
            for d in range(1,4):
                for inds in combinations(range(4),d):
                    F=tuple(C[i] for i in inds);fk,n=self.face_key(sector,F);Fc=fk[2]
                    perm=[Fc.index(self.T(sector,C[i],(-n[0],-n[1]))) for i in inds]
                    self.ck(sorted(perm)==list(range(d)),'face occurrence vertex permutation')
                    faceocc[fk].append({'cone':cid,'sector':sector,'local_columns':list(inds),
                                        'literal_rays':[rays[i] for i in inds],'period_from_canonical':list(n),
                                        'vertex_permutation_to_canonical':perm})
        faces=[]
        for k,(fk,occ) in enumerate(sorted(faceocc.items()),1):
            tag,d,Fc=fk;sector=occ[0]['sector']
            boundary='H' if all(v[2]==0 for v in Fc) else sector if all(v[3]==0 for v in Fc) else None
            stabilizer=[]
            if boundary=='W':stabilizer=[[-self.b,1]]
            elif boundary=='E':stabilizer=[[1,0]]
            canonids=[rid(sector,v) for v in Fc]
            anchor=occ[0]
            gluings=[]
            for q in occ[1:]:
                delta=[q['period_from_canonical'][i]-anchor['period_from_canonical'][i] for i in (0,1)]
                ap=anchor['vertex_permutation_to_canonical'];bp=q['vertex_permutation_to_canonical']
                perm=[bp.index(x) for x in ap]
                gluings.append({'from_occurrence':0,'to_occurrence':len(gluings)+1,
                                'period_vector':delta,'vertex_permutation':perm})
                # Actual vectors can be recovered from the canonical vectors;
                # this checks the period action even across the common H face.
                for j,jj in enumerate(perm):
                    va=self.T(anchor['sector'],Fc[ap[j]],tuple(anchor['period_from_canonical']))
                    vb=self.T(q['sector'],Fc[bp[jj]],tuple(q['period_from_canonical']))
                    self.ck(self.T(anchor['sector'],va,tuple(delta))==vb,'literal face period/gluing map')
            faces.append({'id':f'f{k}','dimension':d,'orbit_sector':tag,'boundary_tag':boundary,
                          'canonical_rays':canonids,'canonical_vectors':Fc,
                          'period_stabilizer_basis':stabilizer,'occurrences':occ,'anchor_gluings':gluings})
        rayrecords={}
        orbitrecords={}
        for sector in SECTORS:
            rec=[]
            for v,i in literal[sector].items():
                oi,w,n=oid(sector,v)
                self.ck(self.T(sector,w,n)==v,'literal ray reconstructed from orbit and period')
                rec.append({'id':i,'vector':v,'orbit':oi,'period_from_orbit':n,
                            'boundary_tag':'H' if v[2]==0 else sector if v[3]==0 else None,
                            'source_parameter_order':v[3] if sector!='E' else v[2]+v[3]})
            rayrecords[sector]=rec
            orbitrecords[sector]=[{'id':i,'primitive_vector':v,'period_stabilizer_basis':
                                  ([[-self.b,1]] if sector=='W' else [[1,0]]) if v[3]==0 and sector!='I' else []}
                                 for v,i in rayorbits[sector].items()]
        return {'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'parameters':{'a':self.a,'b':self.b,'N':self.N},
                'lattice_order':['Z','V','base0','base1'],'physical_delta':[0,1,0,0],
                'period_matrices':{'I':self.P['I'],'W':self.P['W'],'E':self.P['E'],'H':self.H},
                'period_formula':'T_n(x,r,s)=(x+(r P0+s H)n,r,s)',
                'canonical_period_direction':'literal representative = T_recorded_period(canonical representative)',
                'source_parameter_orders':{'I':'s','W':'s','E':'r+s'},
                'initial_counts':self.initial_counts,'checks':self.checks,'star_steps':len(self.trace),
                'maximal_cone_counts':{s:sum(c['sector']==s for c in cones) for s in SECTORS},
                'ray_orbit_counts':{s:len(rayorbits[s]) for s in SECTORS},
                'literal_rays':rayrecords,'ray_orbits':orbitrecords,'maximal_cones':cones,'face_orbits':faces,
                'protected_boundary':{s:sorted(self.protected[s]) for s in SECTORS},
                'resolution_trace':self.trace,
                'proof':'notes/part3_source_zero_equivariant_resolution_audit.md',
                'scope':'Exact finite regular fan and period-face maps only. No analytic filling or numerical return assigned.'}


def main():
    p=argparse.ArgumentParser();p.add_argument('--case',choices=['1,2,8','2,1,6','all'],default='all');p.add_argument('--progress',type=int,default=100)
    args=p.parse_args()
    cases=[(1,2,8),(2,1,6)] if args.case=='all' else [tuple(map(int,args.case.split(',')))]
    for a,b,N in cases:
        fan=PeriodicFan(a,b,N);fan.initial();fan.resolve(args.progress);out=fan.export()
        dest=ROOT/'code/part3'/f'source_zero_regular_fan_{a}_{b}_{N}.json'
        dest.write_text(json.dumps(out,separators=(',',':'))+'\n')
        print(f'PASS {a},{b},{N}: {out["checks"]} exact checks, {out["star_steps"]} stars, cone counts {out["maximal_cone_counts"]}, ray orbit counts {out["ray_orbit_counts"]}; {dest.stat().st_size} bytes',flush=True)


if __name__=='__main__':main()
