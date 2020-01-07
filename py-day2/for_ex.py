s='python'
for a in s:
    print(a)

b='java'
l=[10,20,30]

for b in l:
    print(b)

print(a,b)

d={'a':10,'b':20}
for k in d:
    print(k)
line='-'*40
print(line)
for k in d.keys():
    print(k,d[k])
print(line)


for v in d.values():
    print(v)

print(line)

for i in d.items():
    print(i,i[0],i[1])
print(line)


for i,j in d.items():
    print(i,j)
print(line)

hosts=['h1','h2','h3']
ips=['ip1','ip2']

z=zip(hosts,ips)
#print(z)
#print(list(z))
print(line)
for h,p in z:
    print(h,p)

print(z)


r1=range(10)
r2=range(1,10)
r3=range(1,10,2)
print(list(r1),list(r2),list(r3),sep='\n')
print(line)

r4=range(10,1,-1)
print(list(r4))

for i in range (2,10,2):
    print(i)
print(line)

for h in range (0,len(hosts)):
    print(hosts[h])
print(line)

for h in hosts[::2]:
    print(h)

comp=['ibm','del1','sap','del2']
for c in comp:
    if c.startswith('del'):
        print('found')
        break
else:
    print('not found')


for i in comp:
    if not i.startswith('del'):
        continue
    if i.startswith('del'):
        print('some logic')
    print('last statement of the loop')







