function runIndependentK90Audit() {
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;};
  const R=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};};
  const add=(a,b)=>R(a.n*b.d+b.n*a.d,a.d*b.d);
  const neg=a=>R(-a.n,a.d);
  const sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>R(a.n*b.n,a.d*b.d);
  const div=(a,b)=>R(a.n*b.d,a.d*b.n);
  const z=()=>R(0n);
  const int=a=>{if(a.d!==1n)throw Error("nonintegral solution "+a.n+"/"+a.d);return a.n;};
  const eq=(a,b,m)=>{if(a!==b)throw Error(m+": "+a+" != "+b);};
  const mm=(A,B)=>[A[0]*B[0]+A[1]*B[2],A[0]*B[1]+A[1]*B[3],A[2]*B[0]+A[3]*B[2],A[2]*B[1]+A[3]*B[3]];
  const mi=A=>{eq(A[0]*A[3]-A[1]*A[2],1n,"det");return [A[3],-A[1],-A[2],A[0]];};
  const Q=[[1n,-1n,0n,1n],[1n,0n,-1n,1n]];
  const vi=(a,b)=>a>b?vi(b,a):[[0,1,2],[null,3,4],[null,null,5]][a][b];
  const local=(P,a,b,N)=>{
    const pi=mi(P), W=[1n,b,-a,N-2n], B=mm(mm(pi,W),P).map(x=>2n*x);
    const l=[B[3]-B[2],B[0]-B[1],B[3]], t=N-1n, x=pi[1], y=pi[3];
    const w=[x,y,-x-y], d=[-x-2n*y,-2n*x-y,x-y];
    const I=w.map((wi,i)=>t*wi+d[i]*(l[i]-t));
    const J=w.map((wi,i)=>t*wi-d[i]*(l[i]-t));
    return {B,l,t,w,d,I,J};
  };
  const makeSystem=(P,a,b,N,selected,c,e)=>{
    const {w,I,J}=local(P,a,b,N),rows=[];
    for (let j=1;j<=2;j++){
      for(let k=0;k<3;k++){
        const row=Array.from({length:10},z);
        row[vi(k,j)]=add(row[vi(k,j)],R(w[j]));
        row[vi(k,0)]=sub(row[vi(k,0)],R(w[0]));
        row[9]=R((k===j?I[j]:0n)-(k===0?I[0]:0n));rows.push(row);
      }
      const row=Array.from({length:10},z);
      row[6+j]=R(w[j]);row[6]=sub(row[6],R(w[0]));row[9]=R(J[j]-J[0]);rows.push(row);
    }
    let r=Array.from({length:10},z);r[vi(selected,selected)]=R(1n);r[9]=R(c);rows.push(r);
    r=Array.from({length:10},z);r[6+selected]=R(1n);r[9]=R(e);rows.push(r);
    return rows;
  };
  const solve=rows=>{
    const original=rows.map(r=>r.map(v=>R(v.n,v.d)));
    let rank=0,pivots=[];
    for(let col=0;col<9;col++){
      let p=rank;while(p<rows.length&&rows[p][col].n===0n)p++;
      if(p===rows.length)continue;
      [rows[rank],rows[p]]=[rows[p],rows[rank]];
      const pivot=rows[rank][col];rows[rank]=rows[rank].map(v=>div(v,pivot));
      for(let r=0;r<rows.length;r++)if(r!==rank&&rows[r][col].n){
        const factor=rows[r][col];rows[r]=rows[r].map((v,k)=>sub(v,mul(factor,rows[rank][k])));
      }
      pivots.push(col);rank++;
    }
    if(rank!==9)throw Error("rank "+rank);
    for(let r=rank;r<rows.length;r++)if(rows[r][9].n)throw Error("inconsistent");
    const result=Array(9);for(let r=0;r<rank;r++)result[pivots[r]]=int(rows[r][9]);
    for(const row of original){
      let lhs=z();for(let k=0;k<9;k++)lhs=add(lhs,mul(row[k],R(result[k])));
      if(sub(lhs,row[9]).n)throw Error("failed original equation");
    }
    return {V:[[result[0],result[1],result[2]],[result[1],result[3],result[4]],[result[2],result[4],result[5]]],D:result.slice(6)};
  };
  const C2=j=>j*(j-1n)/2n;
  const C3=j=>j*(j-1n)*(j-2n)/6n;
  const sourceIndex=(b,j)=>2n*b*C3(j+1n)+(3n-b)*C2(j+1n);
  const wordBack=P0=>{
    let P=P0.slice(), rev=[];
    while(P[1]!==0n){
      const u=P[0],r=-P[1];if(u<=0n||r<=0n)throw Error("noncanonical");
      const i=r>=u?0:1, old=u+r;P=mm(P,mi(Q[i]));rev.push(i);
      if(P[1]!==0n&&!(P[0]-P[1]<old))throw Error("Euclid");
    }
    eq(P[0],1n,"seed first");eq(P[3],1n,"seed last");
    return {j:P[2],word:rev.reverse()};
  };
  const words=[[0],[0,0],[0,1],[0,0,0],[0,0,1],[0,1,0],[0,1,1]];
  const cases=[];let seedSolves=0,targetSolves=0,unitChecks=0,reverseChecks=0;
  for (const aa of [1n,2n]) for(const p of [1n,2n]) for(const k of [0n,1n,3n]) for(const j of [-2n,-1n,0n,1n,2n]){
    const a=aa,b=3n-a,m=4n*p-(a-1n),N=k*m,t=N-1n,mu=2n-a+6n*p*k;
    const S0=sourceIndex(b,j)+k*(a-1n)*(3n*p-1n)-N*C2(j),nu=6n*S0;
    const P0=[1n,0n,j,1n],c=2n*t-2n*mu-2n*nu,e=2n*t-2n*mu+2n*nu;
    const first=solve(makeSystem(P0,a,b,N,0,c,e));seedSolves++;
    const loc0=local(P0,a,b,N);
    const expectedV=[[c,-loc0.I[0],loc0.I[0]],[-loc0.I[0],loc0.I[1],0n],[loc0.I[0],0n,-loc0.I[2]]];
    const expectedD=[e,loc0.J[1]-loc0.J[0],loc0.J[0]-loc0.J[2]];
    for(let i=0;i<3;i++){eq(first.D[i],expectedD[i],"seed D");for(let l=0;l<3;l++)eq(first.V[i][l],expectedV[i][l],"seed V");}
    const results=[];
    for(const word of words){
      let P=P0.slice(), V=first.V.map(r=>r.slice()),D=first.D.slice(),total=S0,incs=[];
      let coeff=[[1n,0n,0n,0n],[0n,1n,0n,0n],[0n,0n,1n,0n],[0n,0n,0n,1n]].map(C=>mm(mm(mi(P0),C),P0));
      const wind=[1n,b,-a,N-2n];
      for(const i of word){
        const c=V[i][i],e=D[i];
        if((e-c)%4n)throw Error("nonintegral single");const increment=(e-c)/4n;
        total+=increment;incs.push(increment);P=mm(P,Q[i]);
        const loc=local(P,a,b,N);if(loc.w.some(x=>x===0n))throw Error("zero target weight");
        const next=solve(makeSystem(P,a,b,N,2,c,2n*c-e));targetSolves++;
        V=next.V;D=next.D;
        eq((D[2]-V[2][2])/4n,-increment,"actual reverse");eq((D[2]-V[2][2])%4n,0n,"reverse integral");reverseChecks++;
        coeff=coeff.map(C=>mm(mm(mi(Q[i]),C),Q[i]));
        for(let z=0;z<4;z++)eq(2n*coeff.reduce((s,C,h)=>s+wind[h]*C[z],0n),loc.B[z],"full monomial winding");unitChecks++;
      }
      const back=wordBack(P);eq(back.j,j,"same vertical seed");
      if(JSON.stringify(back.word)!==JSON.stringify(word))throw Error("word mismatch");
      results.push({word,basis:P.map(String),increments:incs.map(String),integer_sum:String(total),residue:Number((total%28n+28n)%28n),V:V.map(r=>r.map(String)),D:D.map(String)});
    }
    cases.push({a:Number(a),b:Number(b),p:Number(p),k:Number(k),j:Number(j),m:Number(m),N:Number(N),native_seed:[String(mu),String(nu)],physical_seed:[String(mu+nu),String(4n*mu)],seed_V:first.V.map(r=>r.map(String)),seed_D:first.D.map(String),paths:results});
  }
  return {status:"PASS",reviewer:"fourfold",statement:"P3K.90",method:"Fresh BigInt rational Gaussian elimination of the complete 6 symmetric variation plus 3 derivative unknowns at every seed and target; no closed target reconstruction used.",case_count:cases.length,word_count:cases.reduce((s,c)=>s+c.paths.length,0),seed_full_solves:seedSolves,target_full_solves:targetSolves,full_coefficient_monomial_checks:unitChecks,reverse_selected_checks:reverseChecks,parameter_ranges:{a:[1,2],p:[1,2],k:[0,1,3],j:[-2,-1,0,1,2]},scope:"Actual K89 seed and ZA.3–4 formulas supplied verbatim by root; geometric ZA.1–2/5 file has not been read because the execution environment is unavailable.",cases};
}

if (typeof module !== "undefined" && require.main === module) {
  const result = runIndependentK90Audit();
  process.stdout.write(JSON.stringify(result) + "\n");
}

