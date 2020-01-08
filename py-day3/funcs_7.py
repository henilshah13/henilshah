#variable keyword only argument

def add(a,b=10,*c,d,e,**f):
    print('extra values',f)
    r=a+b+sum(c)+d+e+sum(f.values())
    return r

r1=add(10,d=20,e=30)
print(r1)

r2=add(10,20,30,40,50,d=60,e=70,x=80,y=90)
print(r2)

D={'d':50,'e':60,'x':70}
res3=add(10,20,30,40,**D)
print(res3)