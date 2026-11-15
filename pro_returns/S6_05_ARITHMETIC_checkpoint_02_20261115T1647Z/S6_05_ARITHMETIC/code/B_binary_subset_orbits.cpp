// Exact subset orbits under a permutation group, at specified weights.
#include <vector>
#include <array>
#include <iostream>
#include <fstream>
#include <cstdint>
#include <cassert>
int main(int argc,char**argv){int n,g,k;std::cin>>n>>g>>k;assert(n<=24&&argc==2);bool weights[25]={false};for(int i=0,w;i<k;++i){std::cin>>w;weights[w]=true;}std::vector<std::array<std::array<uint32_t,256>,3>> tab(g);for(int s=0;s<g;++s){std::vector<int> p(n);for(int&i:p)std::cin>>i;for(int j=0;j<3;++j)for(int x=0;x<256;++x){uint32_t y=0;for(int b=0;b<8;++b)if(8*j+b<n&&(x>>b)&1)y|=1u<<p[8*j+b];tab[s][j][x]=y;}}uint32_t total=1u<<n;std::vector<uint16_t> ids(total,0);std::vector<uint32_t> queue;int orbit=0;uint64_t points=0;for(uint32_t x=0;x<total;++x)if(!ids[x]&&weights[__builtin_popcount(x)]){++orbit;assert(orbit<65535);ids[x]=orbit;queue.clear();queue.push_back(x);for(size_t i=0;i<queue.size();++i)for(int j=0;j<g;++j){uint32_t a=queue[i],b=tab[j][0][a&255]|tab[j][1][(a>>8)&255]|tab[j][2][a>>16];if(!ids[b]){ids[b]=orbit;queue.push_back(b);}}points+=queue.size();std::cout<<"orbit "<<orbit<<" representative "<<x<<" size "<<queue.size()<<" weight "<<__builtin_popcount(x)<<"\n";}std::ofstream f(argv[1],std::ios::binary);f.write(reinterpret_cast<const char*>(ids.data()),2*ids.size());std::cout<<"points "<<points<<" orbits "<<orbit<<"\n";}
