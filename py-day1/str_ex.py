#string

a='person'
print(a)

b="person's"
print(b)


c='''person's height xyz"'''
print(c)

d=""" person """
print(b,c,d,sep='\n')

s1='hello'
s2='py'
s3=s1+s2
s4=s1*10
print(s3,s4)

line='-'*40
print(line)

e='person\'s'
print(e)

f=r'C:\newfolder\test.py' #raw string
print(f)

g='wel come'
print(g)
print(len(g))
print(g[1])
print(g[1:6]) #start index is inclusive & end index is exclusive
print(g[1:])
print(g[:6])
print(g[:])
h=g[:]
print(id(h),id(g))



#step
print(g[1:6:1])
print(g)

print(g[1:6:2])

print(g[::-1]) #reverse

print(g[6:1:-2])


print(g[-6])
print(g[-7:-2])

print(g[len(g)-4:])
print(g[-4:])


#str
i=10
j=str(i)
k=str('python')
print(i,j,k,sep='\n')


r1=g.startswith('wel')
print(r1)

r3=g.isupper()
print(r3)

r4=g.upper()
print(r4)


l='abc'
r7=l.isalpha()
print(r7)


m='123'
r8=m.isdigit()
print(r8)

p='abc123'
r9=p.isalnum()
print(r9)

r10=p[-3:].isdigit()
print(r10)

r11=g.count('e')
print(r11)

r12=g.index('e')
print(r12)             # if not founf index error

r13=g.find('e')
print(r13)      #if not found -1


r14=g.index('e',3)
print(r14)       


r15=g.index('e',3,8)
print(r15)       

r16=g.rindex('e')
print(r16)  


p=' wel   come  '
r17=p.strip()
r18=p.lstrip()
r19=p.rstrip()
print(r17,r18,r19,sep='\n')

q='[wel[come][]'
r20=q.strip(']w[e')
print(r20)

r21=q.lstrip('w[')
print(r21)

r22=q.rstrip('][e')
print(r22)

r23=g.replace('e','E')
print(r23)


print(g.split())


print(g.split('e'))



x=10
y=20
z=x+y

r26='add of x and y is z'
r27='add of {} and {} is {}'.format(x,y,z)
print(r26)
print(r27)


r28='add of {1} and {0} is {2}'.format(x,y,z)
print(r28)

r29='add of {x} and {y} is {z}'
print(r29)

r29=f'add of {x} and {y} is {z}'
print(r29)

r30='-'.join(g)
print(r30)































































