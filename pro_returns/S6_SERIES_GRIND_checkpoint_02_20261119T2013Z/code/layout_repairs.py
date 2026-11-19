"""Exact presentation-only repairs for measured display overflows.

Only line breaks, display wrappers and table heading widths change. Each rule
names the observed formula and preserves its mathematical tokens.
"""
import re

def break_display(text, marker, breaks):
    pos=text.index(marker)
    start=text.rfind(r'\[',0,pos)
    end=text.index(r'\]',pos)+2
    block=text[start:end]
    content=block[2:-2]
    tagpos=content.find(r'\tag{')
    if tagpos>=0: math,suffix=content[:tagpos],content[tagpos:]
    else: math,suffix=content,''
    already=r'\begin{gathered}' in math
    for before in breaks:
        assert before in math,(marker,before)
        math=math.replace(before,r'\\'+'\n'+before,1)
    if not already:math='\n'+r'\begin{gathered}'+'\n'+math.strip()+'\n'+r'\end{gathered}'+'\n'
    return text[:start]+r'\['+math+suffix+r'\]'+text[end:]

def repair_layout(text,paper):
    rules={
    'I':[
      ('d(n)=\\frac{n-4r_1(n)-3r_2(n)}{12}',[r'U(n)=',r'\quad\epsilon_n=']),
      ('F^2=Fv_0=Fm=0',[r'\quad OF=1']),
      ('(\\partial_z\\log\\mathcal F,\\partial_w\\log\\mathcal F)',[r'\operatorname{Hess}\log\mathcal F='])],
    'II':[
      ('h=ar,\\quad y=-au',[r'r=bh,']),
      ('N=N_{H/Y}=\\OO(a)',[r'\qquad P\in']),
      ('\\mathcal G=\n (\\C_p\\times\\C_w^*\\times\\Delta_t)/',[r'\delta(t)='])],
    'IV':[
      ('f_2=\\frac{y-t-x/2}{x-s}',[r'B_{2,3}(p)=']),
      (r'\tag{R0E.50}',[r'Q=\kappa q']),
      (r'\tag{R0R.1}',[r'\qquad (a,b;m)=']),
      (r'\tag{SC45.7}',[r'S_G=']),
      (r'\tag{C45.4}',[r'\Psi^{-1}',r'\Psi_{\beta}']),
      (r'\tag{C45.8}',[r'\quad g_t=']),
      (r'\tag{C45.37a}',[r'H_{s,z}(q)=']),
      (r'\tag{SCP45.4}',[r'H=d[']),
      (r'\tag{CR45.3}',[r'H=d\{']),
      (r'\tag{CR45.29}',[r'\quad(\tau,\mu,G,\mathcal B)']),
      (r'\tag{CR45.42}',[r'I_i=']),
      (r'\tag{CP45.1}',[r'c=v/(2u)']),
      (r'\tag{CP45.31}',[r'(u_j,b_j,d_j,\gamma_j)=']),
      (r'\tag{CP45.47}',[r'I_i=']),
      (r'\tag{JFP.33}',[r'x=uv+1/4']),
      (r'\tag{JFP.39}',[r'\chi='])],
    'V':[(r'\tag{E.P17}',[r'\quad v_2='])]}
    for n,(marker,breaks) in enumerate(rules.get(paper,[]),1):
        text=break_display(text,marker,breaks)
        pos=text.index(marker);start=text.rfind(r'\[',0,pos)
        text=text[:start]+'\\label{layout:'+paper+':'+str(n)+'}\n'+text[start:]
    if paper=='I':
        before=r'\left|\frac{\wp_\tau(z)}{\pi^2}+\frac13\right|'+'\n &\\le'
        after=r'&\left|\frac{\wp_\tau(z)}{\pi^2}+\frac13\right|\\'+'\n &\\le'
        assert before in text;text=text.replace(before,after,1)
    if paper=='IV':
        text=text.replace(r'\text{primitive ordinary forward map}',r'\substack{\text{primitive ordinary}\\\text{forward map}}',1)
        text=text.replace(r'\text{primitive cap map}',r'\substack{\text{primitive}\\\text{cap map}}',1)
    if paper=='V':
        text=text.replace('$c_*=1.0945402503114027801162682630549457037\\ldots$.',r'\[c_*=1.0945402503114027801162682630549457037\ldots.\]',1)
    return text
