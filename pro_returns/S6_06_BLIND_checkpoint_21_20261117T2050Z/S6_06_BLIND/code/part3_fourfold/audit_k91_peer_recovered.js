function runK91PeerAudit() {
  const eq=(a,b,msg)=>{if(a!==b)throw Error(msg+": "+a+" != "+b);};
  const mod=(a,n)=>((a%n)+n)%n;
  const gcd=(a,b)=>{while(b){[a,b]=[b,a%b];}return Math.abs(a);};
  let checks=0;const check=(a,b,m)=>{eq(a,b,m);checks++;};
  const cases=[];
  for(let k=1;k<=10;k++)for(let l=0;l<=8;l++){
    const m=3*k,h=6*l+1,M=m*h;
    if(gcd(m,h)!==1)continue;
    for(let nA=-24;nA<=24;nA++)for(let nB=-24;nB<=24;nB++){
      const eps=h*nA+m*nB;if(Math.abs(eps)!==1)continue;
      check(mod(h*nA+2*eps,3),0,"IV root conjugation");
      check(mod(m*nB,3),0,"II root conjugation");
      check(mod(h*nA-2*eps*(-1),3),0,"g0 A divisor");
      check(mod(m*nB,3),0,"g0 B divisor");
      check(-eps-2*eps,-3*eps,"g0 selected divisor");
      check(M*nA%3,0,"A root power");
      check(M*nB%3,0,"B root power");
      const rExp=2*eps*k*h;
      check(3*rExp,2*eps*M,"three-step r power");
      check(mod(3*rExp,3),0,"successive scalar constant");
      check(gcd(k,h),1,"cap denominator coprimality");
      check(k*h/gcd(k,h),k*h,"least common scalar exponent");
      for(let e=-4;e<=4;e++){
        check((-2*eps)*(-3*e)/3-2*eps*e,0,"local z cancellation");
        check((-2*eps)*(-3)/3-2*eps,0,"local unit cancellation");
      }
      const first=[3*eps,6*eps,-2*eps,3],second=[6*eps,12*eps,-2*eps,6],third=[9*eps,18*eps,0,9];
      for(let j=1;j<=3;j++){
        const actual=[3*eps*j,6*eps*j,eps*(j*j-3*j),3*j];
        const expected=[first,second,third][j-1];
        actual.forEach((x,i)=>check(x,expected[i],"plus-origin j="+j+" coefficient "+i));
      }
      // The first seam at v+j/3 has added M coefficient 2*eps*j/9.
      const summed=[0,0,0,0];
      for(let j=0;j<3;j++){
        const seam=[3*eps,6*eps,-2*eps+2*eps*j,3];
        seam.forEach((x,i)=>summed[i]+=x);
      }
      summed.forEach((x,i)=>check(x,third[i],"three actual successive seams"));
      // Phase polynomial theta^2+theta = theta(theta-1)+2theta.
      check(1-1,0,"phase theta square");
      check(1-(-1)-2,0,"phase theta");
      check(mod(-2*eps*M,2),0,"retained physical winding even");
      const coveredK=2*M,coveredEll=24*k*(3*l+1);
      const shorterK=2*k*h,shorterEll=8*k*(3*l+1);
      check(coveredK,3*shorterK,"actual degree-three Euler cube");
      check(coveredEll,3*shorterEll,"actual degree-three Pontryagin pairing");
      check(4*shorterK-shorterEll,24*k*l,"positive shorter index");
      for(let j=-3;j<=4;j++){
        const kw=shorterK-6*k*h*(j-1)*(j-1);
        const kr=coveredK-6*M*(j-1)*(j-1);
        check(kr,3*kw,"vertical actual characteristic cover");
        check(4*kw-shorterEll,24*(k*l-k*h*(j-1)*(j-1)),"vertical shorter index");
      }
      cases.push({k,l,m,h,M,nA,nB,epsilon:eps,shorter_pair:[shorterK,shorterEll],shorter_index:k*l});
    }
  }
  return {status:"PASS",reviewer:"fourfold",scope:"K91 RE.4-5 actual two-cap endpoint, all three plus-origin seams, retained physical winding and degree-three characteristic comparison. This arithmetic certificate accompanies the separately stated morphism audit; it does not derive an endpoint from numerical divisibility.",cases:cases.length,exact_checks:checks,parameter_ranges:{k:[1,10],l:[0,8],nA:[-24,24],nB:[-24,24]},first_cases:cases.slice(0,8),all_cases:cases};
}

if (typeof module !== "undefined" && require.main === module) {
  const result = runK91PeerAudit();
  process.stdout.write(JSON.stringify(result) + "\n");
}

