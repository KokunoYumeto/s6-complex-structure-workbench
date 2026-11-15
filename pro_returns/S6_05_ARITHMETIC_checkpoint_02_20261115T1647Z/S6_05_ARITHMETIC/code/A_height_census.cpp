// A second census indexed directly by height z and ideals of 18 z^2-2.
// The first census is indexed by n and ideals of 18 n^2-2; these are
// different slices. Both share exact quadratic-ring arithmetic only.
#define main A_original_census_main
#include "A_census.cpp"
#undef main
int main(int argc,char**argv){
 uint32_t X=argc>1?std::stoull(argv[1]):10000000;
 auto started=std::chrono::steady_clock::now();
 auto f=sieve(3*X+1);std::map<uint32_t,Q>cache;
 uint64_t S=0,A=0,R=0;std::vector<uint32_t>height;
 uint64_t pell=0;Q pn=mul({1,1},{2,1});
 for(uint32_t z=1;z<=X;z++){
  auto v=seeds(z,f,cache);S+=v.size();
  for(Q st:v){uint64_t s=st.a,t=st.b;
   assert(I(s)*s-3*I(t)*t==18*I(z)*z-2);
   if(288*I(s)*s<=289*(18*I(z)*z-2))++A;
   if(t+4ULL*z<s && 4ULL*s<=17ULL*z){
    ++R;height.push_back(z);
    I a=17*I(s)-72*I(z),n=17*I(z)-4*I(s);
    assert(a>0&&n>=0&&a*a-3*I(t)*t-18*n*n==-2);
   }
  }
  while(4ULL*pn.a<=z){++pell;pn=mul(pn,{2,1});}
  assert(R==A+pell-1);
  if(z==10000||z==100000||z==1000000||z==10000000)
   std::cout<<"X="<<z<<" R="<<R<<" arc="<<A<<" Pell="<<pell<<" unrestricted="<<S<<" exact_arc_identity=PASS\n";
 }
 std::ifstream in("S6_05_ARITHMETIC/code/A_census_1e9.u32",std::ios::binary);
 assert(in.good());std::vector<uint32_t> other;uint32_t h;
 while(in.read(reinterpret_cast<char*>(&h),4)){if(h>X)break;other.push_back(h);}
 assert(other==height);
 std::cout<<"direct_height_ideal_census cutoff="<<X<<" count="<<R<<" all_heights_equal_to_independent_n_slices=PASS\n";
 std::cout<<"seconds="<<std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count()<<"\n";
}
