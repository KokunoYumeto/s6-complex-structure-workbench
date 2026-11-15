// Exact orbits on an affine F3^16 fibre, restricted to one quadratic equation.
// Coordinates use disjoint bitplanes; all group operations are over F3.
// The map written to argv[1] assigns each isotropic point its 16-bit orbit ID.
#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <cstdint>
#include <cassert>
#include <chrono>
using U=uint32_t;
const U MASK=65535;
U add(U a,U b){U a1=a&MASK,a2=a>>16,b1=b&MASK,b2=b>>16,az=~(a1|a2),bz=~(b1|b2);return ((a1&bz)|(b1&az)|(a2&b2))&MASK | (((a2&bz)|(b2&az)|(a1&b1))<<16);}
U mult(U a,int k){return k==0?0:k==1?a:(a<<16)|(a>>16);}
U enc(const std::array<int,16>&v){U a=0,b=0;for(int i=0;i<16;++i){if(v[i]%3==1)a|=1u<<i;if(v[i]%3==2)b|=1u<<i;}return a|(b<<16);}
int main(int argc,char**argv){
 auto start=std::chrono::steady_clock::now();int n,ng;std::cin>>n>>ng;assert(n==16&&argc==2);
 std::vector<std::array<std::array<U,256>,4>> tables(ng);std::vector<U> off(ng);
 for(int g=0;g<ng;++g){std::array<U,16> rows;for(int i=0;i<17;++i){std::array<int,16>v;for(int&x:v)std::cin>>x;if(i<16)rows[i]=enc(v);else off[g]=enc(v);}
  for(int k=0;k<4;++k)for(int a=0;a<16;++a)for(int b=0;b<16;++b){U z=0;if(!(a&b))for(int j=0;j<4;++j)z=add(z,mult(rows[4*k+j],((a>>j)&1)+2*((b>>j)&1)));tables[g][k][a|(b<<4)]=z;}}
 int q[16][16],lin[16],con;for(auto&r:q)for(int&x:r)std::cin>>x;for(int&x:lin)std::cin>>x;std::cin>>con;
 std::array<U,65536> tern{};U pow=1;for(int i=0;i<16;++i){for(U j=0;j<(1u<<i);++j)tern[j|(1u<<i)]=tern[j]+pow;pow*=3;}U total=pow;
 auto index=[&](U x){return tern[x&MASK]+2*tern[x>>16];};
 auto action=[&](U x,int g){U a=x&MASK,b=x>>16,z=off[g];for(int k=0;k<4;++k){z=add(z,tables[g][k][(a&15)|((b&15)<<4)]);a>>=4;b>>=4;}return z;};
 auto qvalue=[&](const std::array<int,16>&v){int t=con;for(int i=0;i<16;++i){t+=lin[i]*v[i];for(int j=0;j<16;++j)t+=v[i]*q[i][j]*v[j];}return t%3;};
 std::vector<uint16_t> ids(total,0);std::vector<U> queue;std::array<int,16> v{};U found=0;uint16_t orbit=0;
 for(U num=0;num<total;++num){
  if(!ids[num]&&qvalue(v)==0){assert(orbit<65534);++orbit;U rep=enc(v);assert(index(rep)==num);queue.clear();queue.push_back(rep);ids[num]=orbit;
   for(size_t j=0;j<queue.size();++j){U x=queue[j];for(int g=0;g<ng;++g){U y=action(x,g),k=index(y);assert(k<total);if(!ids[k]){ids[k]=orbit;queue.push_back(y);}}}
   found+=queue.size();std::cout<<"orbit "<<orbit<<" representative "<<num<<" packed "<<rep<<" size "<<queue.size()<<"\n"<<std::flush;
  }
  for(int i=0;i<16;++i){if(++v[i]<3)break;v[i]=0;}
 }
 std::ofstream out(argv[1],std::ios::binary);out.write(reinterpret_cast<const char*>(ids.data()),ids.size()*sizeof(uint16_t));out.close();
 std::cout<<"points "<<found<<" orbits "<<orbit<<" total_fibre "<<total<<" seconds "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"\n";
}
