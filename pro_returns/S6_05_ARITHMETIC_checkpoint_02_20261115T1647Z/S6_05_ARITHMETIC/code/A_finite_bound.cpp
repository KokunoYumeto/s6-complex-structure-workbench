// Exact integer certificate, using only the independently Arb-certified
// enclosure 35362047799/10^12 < C0 < 35362047800/10^12.
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
using I=__int128_t;
bool check(uint64_t x,uint64_t r){
 if(x<10000||x>1000000000)return true;
 const I d=1000000000000LL;
 for(I c:{I(35362047799LL),I(35362047800LL)}){
  I e=I(r)*d-c*x;
  // This guard also certifies that the subsequent products cannot
  // overflow the signed 128-bit range (they are below 6.25e36).
  assert(-I(10000000000000000LL)<e&&e<I(10000000000000000LL));
  if(!(62500*e*e<1849*I(x)*d*d))return false;
 }
 return true;
}
int main(){
 std::ifstream in("S6_05_ARITHMETIC/code/A_census_1e9.u32",std::ios::binary);assert(in.good());
 uint32_t z=0,h;uint64_t r=0,m=0,checked=0;
 while(in.read(reinterpret_cast<char*>(&h),4)){
  if(h!=z){
   if(z){assert(check(z,r));assert(check(z,r-m));++checked;}
   // At a real jump z, both one-sided limits suffice. Between jumps
   // (r-C*x)/sqrt(x) is strictly decreasing.
   z=h;m=0;
  }
  ++m;++r;
 }
 assert(check(z,r));assert(check(z,r-m));++checked;
 assert(check(1000000000,r));
 // The lower endpoint falls inside the same monotonic interval unless
 // it is a jump; recover its count with a separate exact scan.
 in.clear();in.seekg(0);uint64_t r0=0;
 while(in.read(reinterpret_cast<char*>(&h),4)&&h<=10000)++r0;
 assert(check(10000,r0));
 std::cout<<"exact_bound |R(x)-C0*x| < (43/250)*sqrt(x) for every real 10000<=x<=1000000000 PASS\n";
 std::cout<<"occupied_heights_checked="<<checked<<" total_points="<<r<<" R(10000)="<<r0<<" arithmetic=signed_128_bit_integer\n";
}
