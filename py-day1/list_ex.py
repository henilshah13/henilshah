l1 = list ([10,20,30])
l2=[10,12.5,'python',['a','b']]
print(l2)
print(l2[1])
print(l2[2][1])

print(l2[-1:1:-1])

l2.append(200)
print(l2)

l2.insert(2,300)
print(l2)


l3=[10,20]
l4=['a','b']
l5=l3+l4
l6=l3*10
print(l5,l6,sep='\n')
l3.extend(l4)
print(l3)

r1=l5.pop()
print(r1,l5)

r2=l5.pop(2)
print(r2,l5)

r3=l5.remove(20)
print(r3,l5)

del l5[0]
print(l5)


print(l3)
l3[1]='java'
print(l3)


l6=[10,30,20]
l6.sort()
print(l6)
l6.sort(reverse=True)
print(l6)

l8=[10,'a',20,'b']
l8.reverse()
print(l8)

l8.clear()
print(l8)


l=[10,['a','b']]
m=l
n=l.copy()
print(m,n)

import copy
p=copy.deepcopy(l)
print(id(l[0]),id(p[0]))
print(id(l[1]),id(p[1]))











