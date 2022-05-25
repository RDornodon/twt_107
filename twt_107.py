M=10**9+7
for E in[*open(0)][1:]:
 r,*e=E.split();r=int(r)
 while e:o,v,*e=e;v=int(v);r={'+':r+v,'-':r-v,'*':r*v}[o]
 print(r%[M,-M][r<0])