d={'course':'python','dur':10,'loc':'blr'}
print(d['course'])


d['course']=['c++','java']
print(d['course'])


e=d.copy()

r1=d.pop('course')
print(r1,d)

del d['dur']
print(d)

r2=d.popitem()
print(r2,d)


k=e.keys()
v=e.values()
i=e.items()

print(k)
print(v)
print(i)
