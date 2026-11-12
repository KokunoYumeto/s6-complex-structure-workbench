"""Reproducible exact incidence diagrams for CG-S6-05. CC0-1.0."""
from pathlib import Path
from xml.sax.saxutils import escape
import math

root=Path(__file__).resolve().parents[1]
ink='#213844';blue='#315e73';red='#a34f36';green='#487352'

def start(title,description,height):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="620" height="{height}" viewBox="0 0 620 {height}" role="img" aria-labelledby="title desc">',
    '<title id="title">'+escape(title)+'</title>',
    '<desc id="desc">'+escape(description)+'</desc>',
    f'<rect width="620" height="{height}" fill="#fcfaf5"/>']
def text(p,x,y,s,size=23,color=ink):
    p.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Georgia,serif" font-size="{size}" fill="{color}">{escape(s)}</text>')
def line(p,a,b,color=blue,width=3):
    p.append(f'<path d="M{a[0]} {a[1]}L{b[0]} {b[1]}" fill="none" stroke="{color}" stroke-width="{width}"/>')
def circle(p,x,y,r,fill,stroke=blue):
    p.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')

p=start('The six boundary curves and their exact identifications',
        'The top fan retains all six integral ray coordinates. Below is the schematic boundary hexagon: opposite edges are paired, and its vertices form two alternating triple-point classes. The three gluing units are written below.',920)
text(p,310,38,'The fan of E₀ = Bl₃ ℙ²',28)
origin=(310,185);scale=94
rays=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
labels=['(1, 0)','(0, 1)','(−1, 1)','(−1, 0)','(0, −1)','(1, −1)']
colors=[blue,red,green,blue,red,green]
for (x,y),label,col in zip(rays,labels,colors):
    endpoint=(origin[0]+scale*x,origin[1]-scale*y)
    line(p,origin,endpoint,col)
    text(p,origin[0]+1.42*scale*x,origin[1]-1.25*scale*y+8,label,22,col)
circle(p,*origin,4,ink,ink)
text(p,310,333,'Adjacent rays have determinant 1.',22)
text(p,310,369,'Boundary incidence on the normalization',25)
vertices=[(310+132*math.cos(math.pi/6+i*math.pi/3),
           515-132*math.sin(math.pi/6+i*math.pi/3)) for i in range(6)]
# Edges are labelled by their divisor, not by a metric polygon coordinate.
edge_labels=['e₁','e₂','e₂−e₁','−e₁','−e₂','e₁−e₂']
for i,(a,b) in enumerate(zip(vertices,vertices[1:]+vertices[:1])):
    line(p,a,b,colors[i],5)
    mid=((a[0]+b[0])/2,(a[1]+b[1])/2)
    text(p,310+(mid[0]-310)*1.40,515+(mid[1]-515)*1.40+8,edge_labels[i],23,colors[i])
for i,(x,y) in enumerate(vertices):
    circle(p,x,y,9,ink if i%2==0 else '#fcfaf5',ink)
text(p,310,682,'Opposite edges are identified; each has square −1.',21)
text(p,310,716,'● / ○ mark the two triple-point classes.',22)
text(p,310,758,'Exact multipliers in the same edge character',23)
for y,s,col in [(800,'e₁: exp(−2πiμ₀)',blue),
                (842,'e₂: exp(12πiμ₀)',red),
                (884,'e₁−e₂: exp(−2πi(7μ₀+b₀))',green)]:
    text(p,310,y,s,24,col)
p.append('</svg>')
(root/'assets/cusp-boundary.svg').write_text('\n'.join(p)+'\n',encoding='utf-8')

p=start('Resolved elliptic fibres with every multiplicity',
        'The affine E6 intersection graph has multiplicities one two three two one on one chain and two one on the remaining arm. The visible section meets E2 plus and the zero section meets C. Type III has two multiplicity-one components of intersection two.',850)
text(p,310,37,'The resolved fibre over t = 0',28)
text(p,310,72,'Numbers inside nodes are fibre multiplicities.',21)
nodes={'F2':(310,282,3,'F₂'),
       'E1':(210,215,2,'E₁'),'C':(110,148,1,'C'),
       'F1':(410,215,2,'F₁'),'E2-':(510,148,1,'E₂,−'),
       'F3':(310,394,2,'F₃'),'E2+':(310,506,1,'E₂,+')}
edges=[('C','E1'),('E1','F2'),('F2','F1'),('F1','E2-'),('F2','F3'),('F3','E2+')]
for a,b in edges:line(p,nodes[a][:2],nodes[b][:2])
for key,(x,y,m,label) in nodes.items():
    circle(p,x,y,23,'#eef4f3')
    text(p,x,y+8,str(m),25)
    if key in ('F2','F3','E2+'):text(p,x+78,y+8,label,24)
    else:text(p,x,y-35,label,24)
text(p,90,205,'O meets C',20)
text(p,250,566,'P* meets E₂,+',22)
text(p,310,607,'Every curve has square −2; every edge counts 1.',21)
text(p,310,655,'The resolved fibre over t = 1',27)
line(p,(190,719),(430,719))
line(p,(190,727),(430,727))
circle(p,190,723,23,'#eef4f3');circle(p,430,723,23,'#eef4f3')
text(p,190,731,'1',25);text(p,430,731,'1',25)
text(p,190,775,'identity / O',22);text(p,430,775,'D / P*',22)
text(p,310,816,'Both squares are −2; intersection is 2.',22)
p.append('</svg>')
(root/'assets/resolved-elliptic-fibres.svg').write_text('\n'.join(p)+'\n',encoding='utf-8')
