def add1(a,b):
    print('result is :')
    print(a+b+a)
    print('end of res')

def sub1(a,b):
    print('result is :')
    print(a - b)
    print('end of res')

add1(10,20)
sub1(10,20)

def mydec(func):
   # def decorated_func(x,y):
    def decorated_func(*x, **y):
        print('result is :')
        #func(x,y)
        func(*x, **y)
        print('end of res')
    return decorated_func

@mydec
def add2(a,b):
    print(a+b+b)
add2(10,20)


#how @mydec works?
def add3(a,b):
    print(a+b)
f=mydec(add3)
#f is decorated_func
f(100,300)
print(f)



@mydec
def add4(a,b,c):
    print(a+b+c)
add4(10,20,30)