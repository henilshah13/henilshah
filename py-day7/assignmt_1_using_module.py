import assgmt_1_func as af
while True:
    i=input('enter id:')
    i=eval(i)
    l=[10,20,30]
    r=af.dev_id_search(i,l)
    print('result=',r)
    ch=input('quit(y/n)? :')
    if ch=='y':
        break