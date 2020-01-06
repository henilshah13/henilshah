#single line commment

''' multi line comment '''
""" multi line comment  """
#https://docs.python.org/3/library/ - standard library link

#number data type
a=10
b=12.5
c=0x12 #hex
d=0b10101 #bin
e=0o12 #oct

print('hello')
print('result=',a,b,c,d,e,sep='|',end='.')
print('test')#other print function : 1.file= 2.flush=

f=int(20)
print(f)

print(a)
print(id(a))

print(type(a))
print(type(a).__name__)

a=100
print(a)
print(id(a))

b=a #refrence copy
a=200
b=300
#sys.getRefcount
