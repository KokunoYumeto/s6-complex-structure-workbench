/* Bounded-memory central derivative for class-number-one CM twists.
   Copyright 2026.  Reproducible research calculation, no BSD input.
   Compile with GMP and MPFR.  Usage: Crank_cm_stream D d cutoff
   D=11,19,43,67,163; d positive squarefree, d=1 mod 4, gcd(d,D)=1.
   Coefficients are the theta series of the canonical conductor-D^2 curve,
   twisted by the quadratic character of d.  We require root number -1.

   L'(1)=2 sum_{n>=1} a_n E1(2*pi*n/(D*d))/n.
   Exact integral coefficient blocks, exact integer Taylor moments, 384-bit
   real arithmetic.  All method constants and cutoffs are printed below.
*/
#include <gmp.h>
#include <mpfr.h>
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <vector>

constexpr mpfr_rnd_t RN=MPFR_RNDN;
#ifndef WORK_PREC
#define WORK_PREC 384
#endif
#ifndef WORK_RAD
#define WORK_RAD 128
#endif
constexpr int PREC=WORK_PREC, RAD=WORK_RAD, WIDTH=2*WORK_RAD+1, MAXDEG=160;
constexpr int64_t SEGMENT=int64_t(WIDTH)*32768;
constexpr int64_t DIRECT=int64_t(WIDTH)*40;

static int64_t isqrt(int64_t x) {
  if(x<=0) return 0;
  int64_t y=(int64_t)std::sqrt((long double)x);
  while((y+1)*(y+1)<=x)++y;
  while(y*y>x)--y;
  return y;
}
static std::vector<int> legtable(int p) {
  std::vector<int> c(p,-1); c[0]=0;
  for(int a=1;a<p;++a)c[(int64_t(a)*a)%p]=1;
  return c;
}
static std::vector<int> chartable(int d) {
  std::vector<int> c(d,1);
  int r=d;
  for(int p=2;p<=r;++p)if(r%p==0) {
    auto t=legtable(p);
    for(int n=0;n<d;++n)c[n]*=t[n%p];
    r/=p;
    if(r%p==0){std::fprintf(stderr,"d not squarefree\n");std::exit(2);}
  }
  return c;
}
static void make_coeff(std::vector<int32_t>& a,int64_t lo,int64_t hi,
                       int D,int d,const std::vector<int>& chi,
                       const std::vector<int>& twist) {
  std::fill(a.begin(),a.end(),0);
  for(int64_t k=isqrt(lo-1)+1;k*k<=hi;++k)
    a[k*k-lo]+=chi[k%D]*int(k)*twist[(k*k)%d];
  const int inv2=(D+1)/2;
  for(int64_t v=1;D*v*v<4*hi;++v) {
    const int64_t vv=D*v*v;
    int64_t u=std::max<int64_t>(1,isqrt(std::max<int64_t>(0,4*lo-vv)));
    while(u*u+vv<4*lo)++u;
    if((u-v)%2)++u;
    const int64_t top=isqrt(4*hi-vv);
    for(;u<=top;u+=2) {
      int64_t n=(u*u+vv)/4;
      a[n-lo]+=chi[(inv2*u)%D]*int(u)*twist[n%d];
    }
  }
}

int main(int argc,char**argv) {
  const int D=argc>1?std::atoi(argv[1]):163;
  const int d=argc>2?std::atoi(argv[2]):185801;
  const int cutoff=argc>3?std::atoi(argv[3]):170;
  if(d<1||d%4!=1||D%8!=3){std::fprintf(stderr,"bad parameters\n");return 2;}
  const int64_t sqrtN=int64_t(D)*d;
  const int64_t limit=(int64_t)std::ceil((long double)cutoff*sqrtN/(2*acosl(-1)));
  auto chi=legtable(D); auto twist=chartable(d);
  mpfr_set_default_prec(PREC);
  mpfr_t c,x,ex,e1,exstep,s,sp,term,tmp,tmp2,total,scale,invn,advance;
  mpfr_inits(c,x,ex,e1,exstep,s,sp,term,tmp,tmp2,total,scale,invn,advance,(mpfr_ptr)0);
  mpfr_const_pi(c,RN);mpfr_mul_ui(c,c,2,RN);mpfr_div_ui(c,c,sqrtN,RN);
  mpfr_set_zero(total,1);
  mpfr_mul_ui(exstep,c,WIDTH,RN);mpfr_neg(exstep,exstep,RN);mpfr_exp(exstep,exstep,RN);
  mpfr_t ec[MAXDEG+1],gg[MAXDEG+1],phi[MAXDEG+1];
  mpz_t powers[RAD+1][MAXDEG+1],mom[MAXDEG+1];
  for(int k=0;k<=MAXDEG;++k){
    mpfr_init(ec[k]);mpfr_init(gg[k]);mpfr_init(phi[k]);mpz_init(mom[k]);
    for(int r=0;r<=RAD;++r){mpz_init(powers[r][k]);mpz_ui_pow_ui(powers[r][k],r,k);}
  }
  std::vector<int32_t>a(SEGMENT);
  int64_t count=0,blocks=0;uint64_t sumabs=0;int maxabs=0,maxD=0,maxJ=0;
  int64_t center=DIRECT+1+RAD;
  mpfr_mul_ui(x,c,center,RN);mpfr_neg(tmp,x,RN);
  mpfr_exp(ex,tmp,RN);mpfr_eint(e1,tmp,RN);mpfr_neg(e1,e1,RN);
  std::printf("D %d d %d sqrtN %lld cutoff %d limit %lld precision_bits %d\n",D,d,(long long)sqrtN,cutoff,(long long)limit,PREC);
  std::printf("radius %d width %d segment %lld direct %lld Taylor_q_power 1e-85 advance_q_power 1e-110\n",RAD,WIDTH,(long long)SEGMENT,(long long)DIRECT);
  std::fflush(stdout);
  const auto started=std::time(nullptr);
  for(int64_t lo=1;lo<=limit;lo+=SEGMENT) {
    const int64_t hi=std::min<int64_t>(limit,lo+SEGMENT-1);
    make_coeff(a,lo,hi,D,d,chi,twist);
    for(int64_t n=lo;n<=std::min<int64_t>(hi,DIRECT);++n) {
      const int an=a[n-lo];if(!an)continue;
      ++count;sumabs+=std::abs(an);maxabs=std::max(maxabs,std::abs(an));
      mpfr_mul_ui(tmp,c,n,RN);mpfr_neg(tmp,tmp,RN);mpfr_eint(term,tmp,RN);
      mpfr_mul_si(term,term,-an,RN);mpfr_div_ui(term,term,n,RN);
      mpfr_add(total,total,term,RN);
    }
    for(int64_t b=std::max<int64_t>(lo,DIRECT+1);b<=hi;b+=WIDTH) {
      center=b+RAD;
      const double q=2.0*RAD/center, qa=2.0*WIDTH/center;
      int deg=std::max(4,(int)std::ceil(-85.0/std::log10(q))-1);
      int adv=std::max(4,(int)std::ceil(-110.0/std::log10(qa))-1);
      const int work=std::max(deg,adv);
      if(work>MAXDEG){std::fprintf(stderr,"degree overflow\n");return 2;}
      maxD=std::max(maxD,deg);maxJ=std::max(maxJ,adv);
      for(int k=0;k<=deg;++k)mpz_set_ui(mom[k],0);
      for(int r=-RAD;r<=RAD;++r) {
        const int64_t n=center+r;if(n>hi)continue;
        const int an=a[n-lo];if(!an)continue;
        ++count;sumabs+=std::abs(an);maxabs=std::max(maxabs,std::abs(an));
        const unsigned long aa=std::abs(an);const int rr=std::abs(r);
        for(int k=0;k<=deg;++k) {
          if((an<0)^((r<0)&&(k&1)))mpz_submul_ui(mom[k],powers[rr][k],aa);
          else mpz_addmul_ui(mom[k],powers[rr][k],aa);
        }
      }
      // Refresh from correctly rounded special functions every 1024 blocks.
      // This prevents accumulated continuation error from entering far tails.
      if(blocks%1024==0) {
        mpfr_mul_ui(x,c,center,RN);mpfr_neg(tmp,x,RN);
        mpfr_exp(ex,tmp,RN);mpfr_eint(e1,tmp,RN);mpfr_neg(e1,e1,RN);
      }
      mpfr_set(ec[0],ex,RN);mpfr_set(gg[0],ex,RN);mpfr_set(phi[0],e1,RN);
      for(int k=1;k<=work;++k) {
        mpfr_mul(ec[k],ec[k-1],x,RN);mpfr_div_ui(ec[k],ec[k],k,RN);mpfr_neg(ec[k],ec[k],RN);
        mpfr_sub(gg[k],ec[k],gg[k-1],RN);
        if(k<=deg){mpfr_div_ui(phi[k],gg[k-1],k,RN);mpfr_add(phi[k],phi[k],phi[k-1],RN);mpfr_neg(phi[k],phi[k],RN);}
      }
      mpfr_set_ui(invn,1,RN);mpfr_div_ui(invn,invn,center,RN);mpfr_set(scale,invn,RN);
      for(int k=0;k<=deg;++k) {
        mpfr_set_z(term,mom[k],RN);mpfr_mul(term,term,scale,RN);
        mpfr_mul(term,term,phi[k],RN);mpfr_add(total,total,term,RN);
        mpfr_mul(scale,scale,invn,RN);
      }
      mpfr_mul_ui(s,invn,WIDTH,RN);mpfr_set(sp,s,RN);mpfr_set_zero(advance,1);
      for(int k=0;k<=adv;++k) {
        mpfr_mul(term,gg[k],sp,RN);mpfr_div_ui(term,term,k+1,RN);
        mpfr_add(advance,advance,term,RN);mpfr_mul(sp,sp,s,RN);
      }
      mpfr_sub(e1,e1,advance,RN);mpfr_mul(ex,ex,exstep,RN);
      mpfr_mul_ui(tmp,c,WIDTH,RN);mpfr_add(x,x,tmp,RN);
      ++blocks;
    }
    std::printf("progress %lld / %lld nonzero %lld elapsed %lld sec\n",(long long)hi,(long long)limit,(long long)count,(long long)(std::time(nullptr)-started));std::fflush(stdout);
  }
  mpfr_mul_ui(total,total,2,RN);
  mpfr_printf("Lprime %.100RNf\n",total);
  // Hasse |a_n| <= d(n)*sqrt(n) <= 2n gives this rigorous tail bound.
  mpfr_mul_ui(tmp,c,limit+1,RN);mpfr_neg(tmp2,tmp,RN);mpfr_exp(tmp2,tmp2,RN);
  mpfr_mul_ui(tmp2,tmp2,4,RN);mpfr_div(tmp2,tmp2,tmp,RN);
  mpfr_neg(tmp,c,RN);mpfr_exp(tmp,tmp,RN);mpfr_ui_sub(tmp,1,tmp,RN);
  mpfr_div(tmp2,tmp2,tmp,RN);mpfr_printf("tail_bound %.20RNe\n",tmp2);
  std::printf("stats nonzero %lld sumabs %llu maxabs %d blocks %lld max_moment_degree %d max_advance_degree %d elapsed %lld sec\n",(long long)count,(unsigned long long)sumabs,maxabs,(long long)blocks,maxD,maxJ,(long long)(std::time(nullptr)-started));
  return 0;
}
