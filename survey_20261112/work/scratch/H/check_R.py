import numpy as np, itertools, math
from fractions import Fraction
rng = np.random.default_rng(1)
def L(h):
    a,b,c,d = h
    return np.array([[a,-b,-c,-d],[b,a,-d,c],[c,d,a,-b],[d,-c,b,a]],float)
def qmul(p,q):
    a,b,c,d = p; e,f,g,h = q
    return np.array([a*e-b*f-c*g-d*h, a*f+b*e+c*h-d*g, a*g-b*h+c*e+d*f, a*h+b*g-c*f+d*e])
def conj(p): return np.array([p[0],-p[1],-p[2],-p[3]])
# R1: det L(H) = N(H)^4
def randH():
    G = rng.normal(size=(3,3,4))
    # H = G^* G + I  (quaternionic)
    H = np.zeros((3,3,4))
    for i in range(3):
        for j in range(3):
            s = np.zeros(4)
            for k in range(3):
                s += qmul(conj(G[k,i]), G[k,j])
            H[i,j] = s
        H[i,i,0] += 1
    return H
def real(H):
    M = np.zeros((12,12))
    for i in range(3):
        for j in range(3):
            M[4*i:4*i+4, 4*j:4*j+4] = L(H[i,j])
    return M
def N(H):
    a,b,lam = H[0,0,0],H[1,1,0],H[2,2,0]
    v,q1,q2 = H[0,1],H[0,2],H[1,2]
    return a*b*lam - lam*(v@v) - b*(q1@q1) - a*(q2@q2) + 2*qmul(qmul(conj(q1),v),q2)[0]
for _ in range(3):
    H = randH(); M = real(H)
    print('sym', np.allclose(M,M.T), 'det^(1/4)', np.linalg.det(M)**0.25, 'N', N(H))
# R7: M3 determinant from the six points
def quadrow(v):
    # coefficients of v^* A v in theta_3 order
    row = []
    for i in range(3): row.append(v[i]@v[i])
    for (i,j) in [(0,1),(0,2),(1,2)]:
        for r in range(4):
            e = np.zeros(4); e[r]=1
            row.append(2*qmul(qmul(conj(v[i]),e),v[j])[0])
    return row
one=[1,0,0,0]; z=[0,0,0,0]; I=[0,1,0,0]; J=[0,0,1,0]; K=[0,0,0,1]
V = [ [z,z,z],[one,z,z],[z,one,z],[z,z,one],[z,[0,1,0,1],[1,1,0,0]],[[1,0,1,0],[0,-1,0,0],J] ]
V = [np.array(v,float) for v in V]
rows = [quadrow(V[a]-V[b]) for a,b in itertools.combinations(range(6),2)]
M3 = np.array(rows)
print('det M3', round(np.linalg.det(M3)))
print(M3.astype(int)[3], M3.astype(int)[14])
W = [np.array(w,float) for w in [[z,z],[one,z],[z,one],[[0,-1,0,0],[0,0,-1,0]]]]
def quadrow2(v):
    row=[v[0]@v[0], v[1]@v[1]]
    for r in range(4):
        e=np.zeros(4); e[r]=1
        row.append(2*qmul(qmul(conj(v[0]),e),v[1])[0])
    return row
M2 = np.array([quadrow2(W[a]-W[b]) for a,b in itertools.combinations(range(4),2)])
print('det M2', round(np.linalg.det(M2))); print(M2.astype(int))
# R3/R8
from mpmath import quad, hyp2f1, pi, cos, mpf
m,b = mpf(6), 2*mpf(5)**0.5
print('R3', quad(lambda t: 1/(m-b*cos(t))**2,[0,2*pi])/(2*pi), m/(m*m-b*b)**1.5, 'ratio to 1/m^2', (m/(m*m-b*b)**1.5)*m*m)
for p in (0.7, 2, 3.5):
    print('R8 p',p, quad(lambda t: (m-b*cos(t))**(-p),[0,pi,2*pi])/(2*pi), m**(-p)*hyp2f1(p/2,(p+1)/2,1,b*b/m/m))
# witness H_r
r=2.7
u=np.ones((3,1)); Hr=np.eye(3)+(r-1)/3*u@u.T
print('N(H_r)=det', np.linalg.det(Hr))
# R4 affinity for real diagonal sanity: N(H)N(G)/N((H+G)/2)^2, with r,s : 4rs/(r+s)^2
s=0.9; Hs=np.eye(3)+(s-1)/3*u@u.T
print(np.linalg.det(Hr)*np.linalg.det(Hs)/np.linalg.det((Hr+Hs)/2)**2, 4*r*s/(r+s)**2)
