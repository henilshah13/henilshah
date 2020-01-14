d={'ROM':'it is rom',
      'HDD':'it is hdd',
      'FDD':'it is fdd',
      'RAM':'it is ram',
      'CPU':'it is cpu'}

ch=input('enter device name:')
f=0
we={print(d[i],f=1) for i in sorted(d.keys()) if i==ch}
    
       
    elif i.startswith(ch)==True:
         print(d[i])
         f=1
if f==0:
    print('Device not found')
    
    
