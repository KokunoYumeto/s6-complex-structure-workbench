/* D2 independent recount of the Koide reduced-root count, in ORIGINAL coordinates sliced by height z.
   R(X) = #{(x,y,z) in Z^3 : Delta(x,y,z) = 4(xy+xz+yz)-(x^2+y^2+z^2) = -1, 0<x<=y, 4(x+y)<=z<=X}.
   With s = x+y+4z, t = y-x:  2*Delta = s^2 - 3 t^2 - 18 z^2, so s^2 - 3t^2 = 18z^2 - 2,
   and the conditions become t>=0, s-4z>t, s<=17z/4.  For each z loop s in (sqrt(18z^2-2), 17z/4]. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
static inline uint64_t isqrt64(uint64_t v){ uint64_t r=(uint64_t)sqrtl((long double)v); while(r*r>v) r--; while((r+1)*(r+1)<=v) r++; return r; }
int main(int argc,char**argv){
  int64_t X = argc>1? atoll(argv[1]) : 1000000;
  int64_t step = argc>2? atoll(argv[2]) : X/10;
  int32_t *cnt = calloc(X+1,sizeof(int32_t));
  #pragma omp parallel for schedule(dynamic,4096)
  for(int64_t z=1; z<=X; z++){
    uint64_t m = 18ULL*z*z-2;
    uint64_t lo = isqrt64(m); if(lo*lo<m) lo++;
    uint64_t hi = (17ULL*z)/4;
    int c=0;
    for(uint64_t s=lo; s<=hi; s++){
      if(s%3==0) continue;
      uint64_t d = s*s-m;            /* = 3 t^2 */
      if(d%3) continue;
      uint64_t t2=d/3, t=isqrt64(t2);
      if(t*t!=t2) continue;
      if((int64_t)s-4*z <= (int64_t)t) continue;   /* x>0 */
      if(((s-4*z-t)&1)) continue;                  /* integrality of x,y (automatic) */
      /* recheck in the original polynomial */
      int64_t x=((int64_t)s-4*z-(int64_t)t)/2, y=((int64_t)s-4*z+(int64_t)t)/2;
      __int128 D = (__int128)4*((__int128)x*y+(__int128)x*z+(__int128)y*z) - ((__int128)x*x+(__int128)y*y+(__int128)z*z);
      if(D!=-1 || x<=0 || x>y || 4*(x+y)>z){ fprintf(stderr,"BAD %lld %lld %lld\n",(long long)x,(long long)y,(long long)z); exit(1);}
      c++;
    }
    cnt[z]=c;
  }
  const long double C0 = 9.0L/(2*M_PI*M_PI)*logl(2+sqrtl(3))*logl(3/(2*sqrtl(2)));
  int64_t R=0; long double maxabs=0; int64_t argmax=0; long double maxpos=-1e30,minneg=1e30; int64_t ap=0,an=0;
  int maxmult=0; int64_t zmult=0; int64_t occupied=0;
  for(int64_t z=1; z<=X; z++){
    /* just before z: R const, E decreasing: check E at z-1 handled by previous iteration end; check both sides */
    long double Eb = (long double)R - C0*z;  /* limit from the left at z (R not yet updated) ~ value at z-1 minus C0 */
    if(z>=10000 && fabsl(Eb)/sqrtl((long double)z) > maxabs && cnt[z]==0){ }
    R += cnt[z];
    if(cnt[z]){occupied++; if(cnt[z]>maxmult){maxmult=cnt[z]; zmult=z;}}
    long double E = (long double)R - C0*z;
    if(E>maxpos){maxpos=E;ap=z;} if(E<minneg){minneg=E;an=z;}
    if(z>=10000){ long double r=fabsl(E)/sqrtl((long double)z); if(r>maxabs){maxabs=r;argmax=z;} }
    if(z%step==0 || z==X) printf("X=%lld R=%lld E=%.6Lf E/sqrtX=%.6Lf\n",(long long)z,(long long)R,E,E/sqrtl((long double)z));
  }
  printf("C0=%.18Lf\nmax E=%.6Lf at %lld; min E=%.6Lf at %lld; max|E|/sqrt(X) on [1e4,X]=%.6Lf at %lld\n",C0,maxpos,(long long)ap,minneg,(long long)an,maxabs,(long long)argmax);
  printf("occupied heights=%lld max multiplicity=%d at z=%lld\n",(long long)occupied,maxmult,(long long)zmult);
  /* first roots */
  return 0;
}
