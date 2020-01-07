a=0
if a==10:
    print('a equal to 10')
if a>10:
    print('a greater then 10')
if a<10:
    print('a less than 10')


a=10
if a==10:
    print('a equal to 10')
elif a>10:
    print('a greater then 10')
elif a<10:
    print('a less than 10')


a=5
if a==10:
    print('a equal to 10')
elif a>10:
    print('a greater then 10')
else:
    print('a less than 10')


s='python'
if 'th' in s:
    print('substring found')
if not s.startswith('java'):
    print('not java')
if s!= 'c++':
    print('not c++')
if s[1:3]=='yt':
    print('yt found')

l1=[10,20]
l2=l1
l3=l1.copy()
if 20 in l1:
    print('20 found')
if l1 is l2:
    print('equal')
if id(l1)==id(l2):
    print('botH id equal')
if l1 == l3:
    print('equal')


d={'a':10,'b':20}
if 'b'  in d:
    print('found key-b')
if 'b' in d.keys():
    print('found key-b')
if 20 in d.values():
    print('found value-20')
if ('a',10) in d.items():
    print('found pair')
if 'b'  in d:
    pass

