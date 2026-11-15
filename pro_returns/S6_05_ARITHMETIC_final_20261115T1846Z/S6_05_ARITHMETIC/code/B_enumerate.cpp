// Exhaustive exact shortest-vector enumeration. No floating arithmetic.
// Input D_i are leading principal minors, M_ij=D_{i+1} U_ij.
// q(x)=sum_i (D_{i+1}x_i+sum_{j>i}M_ij*x_j)^2/(D_i D_{i+1}).
// At level i, R=D_{i+1}(B-chosen_suffix) is an integer. The update
// Rnew=(D_i*R-(D_{i+1}x_i+c)^2)/D_{i+1} is integral by Schur complements.
#include <iostream>
#include <vector>
#include <string>
#include <cassert>
#include <chrono>
using I=__int128_t;
using U=__uint128_t;
int n,B,store_vectors;
std::vector<I>D;
std::vector<std::vector<I>>M;
std::vector<long long>x,counts;
unsigned long long nodes=0;
I isqrt(I a){assert(a>=0); U b=a,r=0,bit=U(1)<<126;while(bit>b)bit>>=2;while(bit){if(b>=r+bit){b-=r+bit;r=(r>>1)+bit;}else r>>=1;bit>>=2;}return I(r);}
I floor_div(I a,I b){I q=a/b,r=a%b;return q-(r<0);}
I ceil_div(I a,I b){return -floor_div(-a,b);}
void visit(int i,I R){
 ++nodes;
 I c=0;for(int j=i+1;j<n;++j)c+=M[i][j]*x[j];
 I rad=isqrt(D[i]*R);
 I lo=ceil_div(-rad-c,D[i+1]),hi=floor_div(rad-c,D[i+1]);
 for(I z=lo;z<=hi;++z){
  x[i]=(long long)z;I t=D[i+1]*z+c,nn=D[i]*R-t*t;
  assert(nn>=0 && nn%D[i+1]==0);I next=nn/D[i+1];
  if(i)visit(i-1,next);
  else {long long norm=B-(long long)next;assert(norm>=0&&norm<=B);++counts[norm];
   if(store_vectors&&norm){std::cout<<"vector "<<norm;for(auto v:x)std::cout<<" "<<v;std::cout<<"\n";}}
 }
 x[i]=0;
}
int main(){
 std::cin>>n>>B>>store_vectors;assert(n<=28&&B<=100);
 D.resize(n+1);M.assign(n,std::vector<I>(n));x.resize(n);counts.assign(B+1,0);
 for(auto &a:D){long long z;std::cin>>z;a=z;}
 for(auto &row:M)for(auto&a:row){long long z;std::cin>>z;a=z;}
 auto t=std::chrono::steady_clock::now();visit(n-1,D[n]*B);
 for(int i=0;i<=B;++i)std::cout<<"count "<<i<<" "<<counts[i]<<"\n";
 std::cout<<"nodes "<<nodes<<"\nseconds "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-t).count()<<"\n";
}
