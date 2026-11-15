// Rigorous interval evaluation of L(E,1) for root number +1.
// L(E,1)=2 sum a_n exp(-2*pi*n/sqrt(N))/n.
// Every coefficient and every Taylor moment is integral. MPFR directed
// rounding encloses all arithmetic; an explicit Cauchy remainder encloses
// each block, and Deligne's |a_n|<=2n encloses the infinite tail.
// Usage: B_C6_central_stream CM_DISC SIGNED_TWIST CUTOFF
// or:    B_C6_central_stream --file coefficient_file
// A file begins with conductor N and cutoff M, followed by a_1,...,a_M.
#include <gmp.h>
#include <mpfr.h>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <ctime>
#include <vector>

constexpr int PREC=256,RAD=128,WIDTH=257,MAXK=80;
constexpr int64_t SEGMENT=int64_t(WIDTH)*32768,DIRECT=int64_t(WIDTH)*40;
struct IV {
 mpfr_t lo,hi;
 IV(){mpfr_init2(lo,PREC);mpfr_init2(hi,PREC);mpfr_set_zero(lo,1);mpfr_set_zero(hi,1);}
 IV(const IV& x):IV(){mpfr_set(lo,x.lo,MPFR_RNDD);mpfr_set(hi,x.hi,MPFR_RNDU);}
 IV& operator=(const IV& x){if(this!=&x){mpfr_set(lo,x.lo,MPFR_RNDD);mpfr_set(hi,x.hi,MPFR_RNDU);}return *this;}
 ~IV(){mpfr_clear(lo);mpfr_clear(hi);}
};
IV integer(long n){IV z;mpfr_set_si(z.lo,n,MPFR_RNDD);mpfr_set_si(z.hi,n,MPFR_RNDU);return z;}
IV operator+(const IV&a,const IV&b){IV z;mpfr_add(z.lo,a.lo,b.lo,MPFR_RNDD);mpfr_add(z.hi,a.hi,b.hi,MPFR_RNDU);return z;}
IV operator-(const IV&a){IV z;mpfr_neg(z.lo,a.hi,MPFR_RNDD);mpfr_neg(z.hi,a.lo,MPFR_RNDU);return z;}
IV operator-(const IV&a,const IV&b){return a+(-b);}
IV operator/(const IV&a,unsigned long n){assert(n);IV z;mpfr_div_ui(z.lo,a.lo,n,MPFR_RNDD);mpfr_div_ui(z.hi,a.hi,n,MPFR_RNDU);return z;}
IV operator*(const IV&a,const IV&b){IV z;mpfr_t t;mpfr_init2(t,PREC);mpfr_set_inf(z.lo,1);mpfr_set_inf(z.hi,-1);
 for(int i=0;i<2;++i)for(int j=0;j<2;++j){auto x=i?a.hi:a.lo;auto y=j?b.hi:b.lo;mpfr_mul(t,x,y,MPFR_RNDD);if(mpfr_less_p(t,z.lo))mpfr_set(z.lo,t,MPFR_RNDD);mpfr_mul(t,x,y,MPFR_RNDU);if(mpfr_greater_p(t,z.hi))mpfr_set(z.hi,t,MPFR_RNDU);}mpfr_clear(t);return z;}
IV expi(const IV&a){IV z;mpfr_exp(z.lo,a.lo,MPFR_RNDD);mpfr_exp(z.hi,a.hi,MPFR_RNDU);return z;}
IV mulz(const IV&a,const mpz_t n){IV z;if(mpz_sgn(n)>=0){mpfr_mul_z(z.lo,a.lo,n,MPFR_RNDD);mpfr_mul_z(z.hi,a.hi,n,MPFR_RNDU);}else{mpfr_mul_z(z.lo,a.hi,n,MPFR_RNDD);mpfr_mul_z(z.hi,a.lo,n,MPFR_RNDU);}return z;}
int64_t isqrt(int64_t x){if(x<=0)return 0;int64_t y=std::sqrt((long double)x);while((y+1)*(y+1)<=x)++y;while(y*y>x)--y;return y;}
std::vector<int> legtable(int p){std::vector<int> z(p,-1);z[0]=0;for(int a=1;a<p;++a)z[(int64_t)a*a%p]=1;return z;}
std::vector<int> chartable(int d){std::vector<int> z(d,1);int r=d;for(int p=3;p<=r;++p)if(r%p==0){auto t=legtable(p);for(int n=0;n<d;++n)z[n]*=t[n%p];r/=p;assert(r%p);}assert(r==1);return z;}
void coefficients(std::vector<int64_t>&a,int64_t lo,int64_t hi,int D,int d,const std::vector<int>&chi,const std::vector<int>&twist){
 std::fill(a.begin(),a.end(),0);
 for(int64_t k=isqrt(lo-1)+1;k*k<=hi;++k)a[k*k-lo]+=chi[k%D]*k*twist[(k*k)%d];
 int inv2=(D+1)/2;
 for(int64_t v=1;D*v*v<4*hi;++v){int64_t vv=D*v*v;int64_t u=std::max<int64_t>(1,isqrt(std::max<int64_t>(0,4*lo-vv)));while(u*u+vv<4*lo)++u;if((u-v)%2)++u;int64_t top=isqrt(4*hi-vv);for(;u<=top;u+=2){int64_t n=(u*u+vv)/4;a[n-lo]+=chi[(inv2*u)%D]*u*twist[n%d];}}
}
int main(int argc,char**argv){
 bool fromfile=argc==3&&!std::strcmp(argv[1],"--file");
 if(!fromfile&&argc!=4)return 2;
 uint64_t N=0;int64_t limit=0;int D=0,d=0,tw=0,cutoff=0;std::ifstream input;
 std::vector<int> chi,twist;
 if(fromfile){input.open(argv[2]);input>>N>>limit;assert(input&&N&&limit>0);}
 else{D=std::atoi(argv[1]);tw=std::atoi(argv[2]);cutoff=std::atoi(argv[3]);d=std::abs(tw);assert(D%8==3&&d>1&&d%2&&((tw%4+4)%4)==1);uint64_t sn=(uint64_t)D*d;N=sn*sn;limit=std::ceil((long double)cutoff*sn/(2*acosl(-1)));chi=legtable(D);twist=chartable(d);}
 IV c,sn,pi;mpfr_set_ui(sn.lo,N,MPFR_RNDD);mpfr_set_ui(sn.hi,N,MPFR_RNDU);mpfr_sqrt(sn.lo,sn.lo,MPFR_RNDD);mpfr_sqrt(sn.hi,sn.hi,MPFR_RNDU);mpfr_const_pi(pi.lo,MPFR_RNDD);mpfr_const_pi(pi.hi,MPFR_RNDU);pi=pi*integer(2);mpfr_div(c.lo,pi.lo,sn.hi,MPFR_RNDD);mpfr_div(c.hi,pi.hi,sn.lo,MPFR_RNDU);
 IV total,step=expi(-(c*integer(WIDTH))),ex=expi(-(c*integer(DIRECT+1+RAD)));
 mpz_t powers[RAD+1][MAXK+1],mom[MAXK+1];for(int k=0;k<=MAXK;++k){mpz_init(mom[k]);for(int r=0;r<=RAD;++r){mpz_init(powers[r][k]);mpz_ui_pow_ui(powers[r][k],r,k);}}
 mpfr_t rem,err,q,powq,den,tmp,tail;mpfr_inits2(PREC,rem,err,q,powq,den,tmp,tail,(mpfr_ptr)0);mpfr_set_zero(err,1);
 std::vector<int64_t>a(SEGMENT);int64_t blocks=0,nonzero=0;int maxk=0;auto started=std::time(nullptr);
 std::printf("CERTIFIED central value conductor %llu limit %lld precision_bits %d D %d signed_twist %d\n",(unsigned long long)N,(long long)limit,PREC,D,tw);std::fflush(stdout);
 for(int64_t lo=1;lo<=limit;lo+=SEGMENT){int64_t hi=std::min(limit,lo+SEGMENT-1);
  if(fromfile){for(int64_t n=lo;n<=hi;++n){input>>a[n-lo];assert(input);}}
  else coefficients(a,lo,hi,D,d,chi,twist);
  for(int64_t n=lo;n<=std::min(hi,DIRECT);++n)if(a[n-lo]){++nonzero;total=total+expi(-(c*integer(n)))*integer(a[n-lo])/n;}
  for(int64_t b=std::max(lo,DIRECT+1);b<=hi;b+=WIDTH){int64_t center=b+RAD;double qd=2.0*RAD/center;int kmax=std::max(2,(int)std::ceil(-40/std::log10(qd))-1);assert(kmax<=MAXK);maxk=std::max(maxk,kmax);for(int k=0;k<=kmax;++k)mpz_set_ui(mom[k],0);
   uint64_t absum=0;
   for(int64_t n=b;n<=std::min(hi,b+WIDTH-1);++n){int64_t an=a[n-lo];if(!an)continue;++nonzero;assert(std::abs(an)<=2*n);absum+=std::abs(an);int r=n-center;for(int k=0;k<=kmax;++k){bool neg=(an<0)^((r<0)&&(k%2));if(neg)mpz_submul_ui(mom[k],powers[std::abs(r)][k],std::abs(an));else mpz_addmul_ui(mom[k],powers[std::abs(r)][k],std::abs(an));}}
   IV cpow=integer(1),t=integer(1)/center,pol=mulz(t,mom[0]);
   for(int k=1;k<=kmax;++k){cpow=cpow*c/k;t=(t+cpow)/center;IV z=mulz(t,mom[k]);pol=pol+(k%2?-z:z);}
   total=total+ex*pol;
   // On |z|=center/2, |exp(-c(center+z))/(center+z)|
   // <=2 exp(-c center/2)/center. Cauchy's formula gives the tail.
   mpfr_set_ui(q,2*RAD,MPFR_RNDU);mpfr_div_ui(q,q,center,MPFR_RNDU);mpfr_pow_ui(powq,q,kmax+1,MPFR_RNDU);mpfr_ui_sub(den,1,q,MPFR_RNDD);mpfr_sqrt(rem,ex.hi,MPFR_RNDU);mpfr_mul_ui(rem,rem,2,MPFR_RNDU);mpfr_div_ui(rem,rem,center,MPFR_RNDU);mpfr_mul(rem,rem,powq,MPFR_RNDU);mpfr_div(rem,rem,den,MPFR_RNDU);mpfr_mul_ui(rem,rem,absum,MPFR_RNDU);mpfr_add(err,err,rem,MPFR_RNDU);
   ex=ex*step;++blocks;
  }
  std::printf("progress %lld/%lld elapsed %ld sec\n",(long long)hi,(long long)limit,(long)(std::time(nullptr)-started));std::fflush(stdout);
 }
 // Infinite tail <=4 exp(-c(M+1))/(1-exp(-c)), evaluated upward.
 mpfr_mul_ui(tmp,c.lo,limit+1,MPFR_RNDD);mpfr_neg(tmp,tmp,MPFR_RNDU);mpfr_exp(tail,tmp,MPFR_RNDU);mpfr_mul_ui(tail,tail,4,MPFR_RNDU);mpfr_neg(tmp,c.lo,MPFR_RNDU);mpfr_exp(tmp,tmp,MPFR_RNDU);mpfr_ui_sub(den,1,tmp,MPFR_RNDD);mpfr_div(tail,tail,den,MPFR_RNDU);
 mpfr_sub(total.lo,total.lo,err,MPFR_RNDD);mpfr_add(total.hi,total.hi,err,MPFR_RNDU);total=total*integer(2);mpfr_sub(total.lo,total.lo,tail,MPFR_RNDD);mpfr_add(total.hi,total.hi,tail,MPFR_RNDU);
 std::printf("nonzero %lld blocks %lld max_degree %d\n",(long long)nonzero,(long long)blocks,maxk);
 mpfr_printf("Taylor_error_upper %.30RUe\nInfinite_tail_upper %.30RUe\nL_lower %.65RDf\nL_upper %.65RUf\n",err,tail,total.lo,total.hi);
 std::puts("PASS: directed-rounding arithmetic, block Cauchy remainders and infinite tail included.");
}
