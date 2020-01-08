count = 0
def create_add():
    global count
    count+=1

def delete_acc():
    global count
    count-=1

create_add()
create_add()

count=100

delete_acc()
print('total=',count)

def acc():
    c=0
    def ca():
        nonlocal c
        c+=1
    def da():
        nonlocal c
        c-=1
    def ta():
        print('total',c)

    return ca,da,ta

x=(10,20)
x,y=(10,20)
f1,f2,f3=acc()
f1()
f1()
c=100
f2()
f3()
