x=10
def f1():
    x=20 #enclosed scope - acessible by itself and also function inside it
    def f2():
        nonlocal x
        x=30
        global y
        y=100
        print('f2=',x)
    f2()
    print('f1=', x)
f1()
print('global=', x,y)

print(dir(__builtins__))
