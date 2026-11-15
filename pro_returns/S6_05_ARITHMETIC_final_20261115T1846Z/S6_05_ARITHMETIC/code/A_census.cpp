// Independent exact census for S6_05_ARITHMETIC, 2026-11-15.
// Z[sqrt(3)] is norm Euclidean by rounding both rational coefficients.
// Every emitted point is checked in the (s,t,z) coordinates of Part A.
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>
using I=__int128_t; using U=__uint128_t; using ll=long long;
struct Q { ll a,b; bool operator<(const Q&o)const{return std::tie(a,b)<std::tie(o.a,o.b);} bool operator==(const Q&o)const{return a==o.a&&b==o.b;} };
I norm(Q x){return I(x.a)*x.a-3*I(x.b)*x.b;}
ll cast(I x){assert(x>=INT64_MIN&&x<=INT64_MAX);return ll(x);}
Q mul(Q x,Q y){return {cast(I(x.a)*y.a+3*I(x.b)*y.b),cast(I(x.a)*y.b+I(x.b)*y.a)};}
Q neg(Q x){return {-x.a,-x.b};}
int sign(Q x){if(x.a>=0&&x.b>=0)return(x.a||x.b)?1:0;if(x.a<=0&&x.b<=0)return-1;I d=norm(x);return x.a>0?(d>0?1:-1):(d>0?-1:1);}
Q reduce(Q x){I n=norm(x);assert(n!=0);if(sign(x)<0)x=neg(x);for(;;){if(n>0?x.b<0:x.a<0){x=mul(x,{2,1});continue;}if(n>0?I(x.a)<=2*I(x.b):2*I(x.a)>=3*I(x.b)){x=mul(x,{2,-1});continue;}assert(x.a>=0&&x.b>=0);assert(norm(x)==n);return x;}}
ll roundq(I a,I b){if(b<0){a=-a;b=-b;}return cast(a>=0?(a+b/2)/b:-((-a+b/2)/b));}
Q gcdq(Q x,Q y){while(y.a||y.b){I n=norm(y);Q d={roundq(I(x.a)*y.a-3*I(x.b)*y.b,n),roundq(I(x.b)*y.a-I(x.a)*y.b,n)};Q q=mul(d,y);Q r={x.a-q.a,x.b-q.b};assert((norm(r)<0?-norm(r):norm(r))<(n<0?-n:n));x=y;y=r;}return reduce(x);}
uint64_t power(uint64_t a,uint64_t n,uint64_t p){uint64_t r=1;for(;n;n>>=1,a=a*a%p)if(n&1)r=r*a%p;return r;}
uint64_t sqrtmod(uint64_t a,uint64_t p){assert(p>2&&power(a,(p-1)/2,p)==1);if(p%4==3)return power(a,(p+1)/4,p);uint64_t q=p-1,s=0;while(!(q&1)){q>>=1;++s;}uint64_t z=2;while(power(z,(p-1)/2,p)!=p-1)++z;uint64_t c=power(z,q,p),x=power(a,(q+1)/2,p),t=power(a,q,p),m=s;while(t!=1){uint64_t i=1,v=t*t%p;while(v!=1){v=v*v%p;++i;}assert(i<m);uint64_t b=power(c,1ULL<<(m-i-1),p);x=x*b%p;t=t*b%p*b%p;c=b*b%p;m=i;}return x;}
uint64_t isqrt(U x){uint64_t r=sqrtl((long double)x);while(U(r)*r>x)--r;while(U(r+1)*(r+1)<=x)++r;return r;}
std::vector<uint32_t> sieve(uint32_t m){std::vector<uint32_t> f(m+1);for(uint32_t p=2;p<=m;p++)if(f[p]==0){f[p]=p;if(uint64_t(p)*p<=m)for(uint64_t n=uint64_t(p)*p;n<=m;n+=p)if(!f[n])f[n]=p;}return f;}
std::vector<std::pair<uint32_t,int>> factors(uint32_t a,uint32_t b,const std::vector<uint32_t>&f){std::vector<uint32_t> p={2};for(uint32_t v:{a,b})while(v>1){p.push_back(f[v]);v/=f[v];}std::sort(p.begin(),p.end());std::vector<std::pair<uint32_t,int>> r;for(auto q:p){if(r.empty()||r.back().first!=q)r.push_back({q,1});else ++r.back().second;}return r;}
Q powred(Q a,int e){Q r={1,0};for(int k=0;k<e;k++)r=reduce(mul(r,a));return r;}
std::vector<Q> seeds(uint32_t n,const std::vector<uint32_t>&f,std::map<uint32_t,Q>&cache){auto fac=factors(3*n-1,3*n+1,f);ll scalar=1;for(auto [p,e]:fac)if(p%12==5||p%12==7){if(e&1)return {};for(int j=0;j<e/2;j++)scalar*=p;}std::vector<Q> v={{scalar,0}};for(auto[p,e]:fac){if(p%12==5||p%12==7)continue;assert(p!=3);Q pi;if(p==2){pi={1,1};Q y=powred(pi,e);for(auto &x:v)x=reduce(mul(x,y));continue;}auto it=cache.find(p);if(it==cache.end()){uint64_t r=sqrtmod(3,p);pi=gcdq({ll(p),0},{ll(r),1});assert(norm(pi)==I(p)||norm(pi)==-I(p));cache[p]=pi;}else pi=it->second;Q bar={pi.a,-pi.b};std::vector<Q> options;for(int k=0;k<=e;k++)options.push_back(reduce(mul(powred(pi,k),powred(bar,e-k))));std::vector<Q> w;for(Q x:v)for(Q y:options)w.push_back(reduce(mul(x,y)));v.swap(w);}std::sort(v.begin(),v.end());assert(std::unique(v.begin(),v.end())==v.end());for(Q x:v){assert(norm(x)==18*I(n)*n-2);assert(x.a>2*x.b&&x.b>=0);}return v;}
void addpoint(uint64_t a,uint64_t q,uint64_t n,uint64_t X,std::vector<uint32_t>&heights){if(a+4*n<=q)return;uint64_t z=4*a+17*n;if(z>X)return;uint64_t s=17*a+72*n,t=q;assert(I(s)*s-3*I(t)*t-18*I(z)*z==-2);assert(t+4*z<s&&4*s<=17*z);assert((s-4*z-t)%2==0);uint64_t x=(s-4*z-t)/2,y=(s-4*z+t)/2;assert(4*(I(x)*y+I(x)*z+I(y)*z)-I(x)*x-I(y)*y-I(z)*z==-1);heights.push_back(z);}
std::vector<uint32_t> literal(uint32_t X){std::vector<uint32_t> h;for(uint64_t z=1;z<=X;z++){U m=18*U(z)*z-2;uint64_t lo=isqrt(m);if(U(lo)*lo<m)++lo;for(uint64_t s=lo;4*s<=17*z;s++){U d=U(s)*s-m;if(d%3)continue;uint64_t t=isqrt(d/3);if(U(t)*t!=d/3)continue;if(t+4*z>=s)continue;h.push_back(z);}}return h;}
int main(int argc,char**argv){uint32_t X=argc>1?std::stoull(argv[1]):10000000;uint32_t brute=argc>2?std::stoull(argv[2]):30000;std::string stem=argc>3?argv[3]:"A_census";auto start=std::chrono::steady_clock::now();uint32_t hi=X/17,lo=0;while(lo<hi){uint32_t m=lo+(hi-lo+1)/2;uint64_t a=isqrt(18*U(m)*m-2);if(I(a)*a<18*I(m)*m-2)++a;if(4*a+17ULL*m<=X)lo=m;else hi=m-1;}uint32_t N=lo;std::cerr<<"n_max="<<N<<" spf_max="<<3*N+1<<"\n";auto f=sieve(3*N+1);std::map<uint32_t,Q>cache;std::vector<uint32_t>heights;heights.reserve(uint64_t(X)/25+100);uint64_t orbits=0;Q pn={1,1};while(4*pn.a<=X){addpoint(pn.a,pn.b,0,X,heights);pn=mul(pn,{2,1});}
for(uint32_t n=1;n<=N;n++){auto v=seeds(n,f,cache);orbits+=v.size();for(Q x:v){for(;4*uint64_t(x.a)+17ULL*n<=X;x=mul(x,{2,1}))addpoint(x.a,x.b,n,X,heights);}if(n%1000000==0)std::cerr<<"n="<<n<<" points="<<heights.size()<<" seconds="<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"\n";}
std::sort(heights.begin(),heights.end());if(brute>X)brute=X;auto h=literal(brute);auto end=std::upper_bound(heights.begin(),heights.end(),brute);assert(std::vector<uint32_t>(heights.begin(),end)==h);std::cout<<"literal_height_slice_check cutoff="<<brute<<" count="<<h.size()<<" PASS\n";std::cout<<"n_max="<<N<<" norm_ideals="<<orbits<<" prime_generators="<<cache.size()<<"\n";long double pi=acosl(-1.0L),C=9/(2*pi*pi)*logl(2+sqrtl(3))*logl(3/(2*sqrtl(2)));std::cout.precision(18);std::cout<<"C0="<<C<<"\n";for(uint32_t y:{10000U,100000U,1000000U,10000000U,100000000U,1000000000U})if(y<=X){uint64_t R=std::upper_bound(heights.begin(),heights.end(),y)-heights.begin();std::cout<<"X="<<y<<" R="<<R<<" E="<<(R-C*y)<<" standardized="<<(R-C*y)/sqrtl(y)<<"\n";}std::cout<<"FINAL X="<<X<<" R="<<heights.size()<<" seconds="<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"\n";std::ofstream file(stem+".u32",std::ios::binary);file.write(reinterpret_cast<const char*>(heights.data()),heights.size()*4);std::cout<<"sorted_heights_file="<<stem<<".u32 uint32_native_little_endian records="<<heights.size()<<"\n";return 0;}
