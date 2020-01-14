list1=[1,3,5,16,8]
list2=[6,5,9,4,13,12]
list3=list1+list2
list3=list(set(list3))
print(list3)

def search(a):
    if s in list3:
        a=list3.index(s)
        print('index position is :',a)
    else:
        for j in list3:
            if j > a:
                print('number is',j,'index is',list3.index(j))
                break
        else:
            print('not found')

s=input('enter device id :')
s=int(s)
search(s)
