f1=open('log_report.txt','w')
f2=open('log_report.csv','w')

f1.write('ip\t\t\t\t\tdate\t\tpics\t\t\turl\n')
f2.writelines(['ip,\t\t\t\t\t','date,\t\t','pics,\t\t\t','url\n'])
f3=open(r'C:\pythontraining\log\serverlog.txt')

for line in f3:
    if line[:3].isdigit():
        #print(line)
        sp=line.split()
        #print(sp)
        ip=sp[0]
        #print(ip)
        dt=sp[3]
        dt2=dt[1:dt.index(':')]
        #print(ip,dt2)
        if  sp[6].startswith('/pics'):
            im=sp[6]
            im1=im[6:]
            #im2=im.split('/')
            #im2=im2[-1]
            im3=im.lstrip('/pics/')
            #im4=im.replace('/pics/','')
            #print(ip, dt2,im3)
        else:
            im3='no image'


        url=sp[10][1:-1]
        print(ip, dt2,im1,url,sep='\t',file=f1)
        print(ip, dt2, im1, url, sep='\,', file=f2)