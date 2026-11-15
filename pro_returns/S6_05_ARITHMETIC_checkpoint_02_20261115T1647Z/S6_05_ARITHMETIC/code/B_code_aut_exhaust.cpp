// Complete monomial automorphism search for a rank-five ternary code.
// Exhaust linear images of five pivot columns, then all permutations in
// projectively repeated coordinate fibres.  Repeated columns are essential.
#include <iostream>
#include <array>
#include <vector>
#include <algorithm>
using V=std::array<int,5>;
V col[12],images[5];std::vector<V> reps;std::vector<std::vector<int>> fibres;
int lookup[243],cl[12],sg[12],target[12],targetsg[12];long long count=0,linear=0,attempt=0;
int code(V a){int s=0,p=1;for(int x:a){s+=x*p;p*=3;}return s;}
V neg(V a){for(auto&x:a)x=(3-x)%3;return a;}
void output(int j,int p[],int signs[]){
 if(j==(int)fibres.size()){++count;std::cout<<"automorphism";for(int k=0;k<12;++k)std::cout<<" "<<p[k]<<":"<<signs[k];std::cout<<"\n";return;}
 std::vector<int> src;for(int k=0;k<12;++k)if(target[k]==j)src.push_back(k);
 auto dst=fibres[j];do{for(int k=0;k<(int)src.size();++k){p[src[k]]=dst[k];signs[src[k]]=targetsg[src[k]]^sg[dst[k]];}output(j+1,p,signs);}while(std::next_permutation(dst.begin(),dst.end()));
}
void test(){
 ++attempt;std::vector<int> used(reps.size(),0);
 for(int k=0;k<12;++k){V a={0,0,0,0,0};for(int j=0;j<5;++j)if(col[k][j])for(int i=0;i<5;++i)a[i]=(a[i]+col[k][j]*images[j][i])%3;
  int z=lookup[code(a)];if(z<0)return;int idx=z/2;if(++used[idx]>(int)fibres[idx].size())return;target[k]=idx;targetsg[k]=z%2;}
 ++linear;int p[12],signs[12];output(0,p,signs);
}
void rec(int j,int used){if(j==5){test();return;}for(int k=0;k<(int)reps.size();++k)if(!((used>>k)&1)){images[j]=reps[k];rec(j+1,used|(1<<k));images[j]=neg(reps[k]);rec(j+1,used|(1<<k));}}
int main(){for(int i=0;i<243;++i)lookup[i]=-1;for(int i=0;i<5;++i)for(int j=0;j<12;++j)std::cin>>col[j][i];for(int k=0;k<12;++k){if(lookup[code(col[k])]<0){int n=reps.size();V a=col[k];for(int x:a)if(x){if(x==2)a=neg(a);break;}reps.push_back(a);fibres.push_back({});lookup[code(a)]=2*n;lookup[code(neg(a))]=2*n+1;}int z=lookup[code(col[k])];cl[k]=z/2;sg[k]=z%2;fibres[cl[k]].push_back(k);}rec(0,0);std::cout<<"projective_classes "<<reps.size()<<"\nattempted "<<attempt<<"\nlinear_maps "<<linear<<"\norder "<<count<<"\n";}
