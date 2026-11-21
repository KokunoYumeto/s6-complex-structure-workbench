// Full saturation, with automatic index bounds, of the known rational points.
// Uses eclib 20250122; algebraic ranks are separately certified by 2-descent.
#include <eclib/saturate.h>
#include <eclib/points.h>
#include <iostream>
#include <string>

static void one(const char* j,const char* a3,const char* a4,const char* a6,
                const char* yy) {
  Curvedata E(to_ZZ(0),to_ZZ(0),to_ZZ(a3),to_ZZ(a4),to_ZZ(a6),0);
  Point P(E,to_ZZ(0),to_ZZ(yy),to_ZZ(1));
  std::cout<<"\nJ "<<j<<" curve "<<E<<" point "<<P<<" valid "<<P.isvalid()<<std::endl;
  std::vector<Point> pp{P};
  saturator S(&E,1,2);S.set_points(pp);
  std::cout<<"automatic_index_bound "<<S.get_index_bound()<<std::endl;
  std::vector<long> unsat;long index=0;
  int status=S.saturate(unsat,index,-1,2,20);
  std::cout<<"status "<<status<<" index "<<index<<" remaining_primes";
  for(auto p:unsat)std::cout<<" "<<p;
  std::cout<<"\ngenerators ";for(auto Q:S.getgens())std::cout<<Q<<" ";std::cout<<std::endl;
}
int main(){
  set_precision(200);initprimes("",0);
  one("54000","0","-7260","234256","484");
  one("287496","0","-2156","38416","196");
  one("16581375","0","-7732620","8275904784","90972");
  one("-3375","0","-140","784","28");
  one("-32768","1","-3234","72630","269");
  one("-884736","1","-38","90","9");
  one("-884736000","1","-379260","89898842","9481");
  one("-147197952000","1","-347045930","2488447882842","1577481");
  one("-262537412640768000","1","-75065352465446420","7916029533155605844266842","2813543945481");
}
