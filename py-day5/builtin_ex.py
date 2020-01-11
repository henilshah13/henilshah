#map
l=[100,200,300,400]

def sub(i):
    return i-10

r1=map(sub,l)
print(list(r1))

#filter

def filt(j):
    return  j>100
r2=filter(filt,l)
print(list(r2))

import _functools as fc
def red(p,q):
    return p+q
r3=fc.reduce(red,l)

m=['w','e','l']
r4=fc.reduce(red,m)
print(r3,r4)

#lambda function
#no name function and single liner


r5=map(lambda i: i-10,l)
r6=filter(lambda j: j>100,l)
r7=fc.reduce(lambda p,q: p+q,l)
print(list(r5))
print(list(r6))
print(r7)
f=lambda a,b:a+b
r8=f(10,20)
print(r8)

l=[(lambda i:i*i)(a) for a in range(10)]
print(l)

keys=['a','b']
values=[10,20]
d={k:(lambda i:i+i)(v) for k,v in zip(keys,values)}
print(d)