// Independent completed-L derivative sums from exact Fourier coefficients.
// 1024-bit MPFR.  For sign -1: L'=2 sum a_n E1(cn)/n.
// For sign +1 and L(1)=0: L''=4 sum a_n G(cn)/n,
// G(x)=int_x^infty exp(-u)log(u/x)/u du.
// Its convergent power series is evaluated with an explicit alternating tail.
#include <gmp.h>
#include <mpfr.h>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <algorithm>

int main(int argc,char**argv){
  if(argc!=2)return 2;
  std::ifstream f(argv[1]);unsigned long N,B;int rank;f>>N>>rank>>B;
  mpfr_set_default_prec(1024);const mpfr_rnd_t R=MPFR_RNDN;
  mpfr_t c,x,term,tmp,g,total,pi,euler,threshold,tail,maxterm;
  mpfr_inits(c,x,term,tmp,g,total,pi,euler,threshold,tail,maxterm,(mpfr_ptr)0);
  mpfr_const_pi(pi,R);mpfr_const_euler(euler,R);
  mpfr_set_ui(c,N,R);mpfr_sqrt(c,c,R);mpfr_div(c,pi,c,R);mpfr_mul_ui(c,c,2,R);
  mpfr_set_zero(total,1);mpfr_set_zero(maxterm,1);mpfr_set_str(threshold,"1e-140",10,R);
  int64_t count=0;int maxk=0;
  for(unsigned long n=1;n<=B;++n){
    long an;f>>an;if(!f){std::fprintf(stderr,"coefficient file ended early\n");return 3;}
    if(!an)continue;++count;mpfr_mul_ui(x,c,n,R);
    if(rank==1){
      mpfr_neg(tmp,x,R);mpfr_eint(g,tmp,R);mpfr_neg(g,g,R);
    }else{
      mpfr_log(g,x,R);mpfr_add(g,g,euler,R);mpfr_sqr(g,g,R);mpfr_div_ui(g,g,2,R);
      mpfr_sqr(tmp,pi,R);mpfr_div_ui(tmp,tmp,12,R);mpfr_add(g,g,tmp,R);
      mpfr_neg(term,x,R);mpfr_add(g,g,term,R);
      for(int k=1;;++k){
        mpfr_mul(term,term,x,R);mpfr_neg(term,term,R);
        mpfr_mul_ui(term,term,k*k,R);mpfr_div_ui(term,term,(k+1)*(k+1)*(k+1),R);
        mpfr_add(g,g,term,R);mpfr_abs(tmp,term,R);
        if(mpfr_greater_p(tmp,maxterm))mpfr_set(maxterm,tmp,R);
        if(k>mpfr_get_d(x,R)&&mpfr_less_p(tmp,threshold)){maxk=std::max(maxk,k+1);break;}
      }
    }
    mpfr_mul_si(term,g,an,R);mpfr_div_ui(term,term,n,R);mpfr_add(total,total,term,R);
  }
  mpfr_mul_ui(total,total,rank==1?2:4,R);
  mpfr_mul_ui(x,c,B+1,R);mpfr_neg(tmp,x,R);mpfr_exp(tail,tmp,R);
  mpfr_div(tail,tail,x,R);if(rank==2)mpfr_div(tail,tail,x,R);
  mpfr_mul_ui(tail,tail,rank==1?4:8,R);
  mpfr_neg(tmp,c,R);mpfr_exp(tmp,tmp,R);mpfr_ui_sub(tmp,1,tmp,R);mpfr_div(tail,tail,tmp,R);
  std::printf("file %s conductor %lu derivative_order %d cutoff %lu nonzero %lld\n",argv[1],N,rank,B,(long long)count);
  mpfr_printf("derivative %.90RNf\ntail_bound %.20RNe\n",total,tail);
  std::printf("precision_bits 1024 G_series_max_terms %d G_series_cutoff 1e-140\n",maxk);
  mpfr_printf("G_series_max_abs_term %.10RNe\n",maxterm);
}
