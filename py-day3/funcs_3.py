#positional args

def add(a,b):
    return a+b

r1=add(10,20)
print(r1)


def get_ips(filepath,mode):
    f=open(filepath)
    if filepath.endswith('.csv'):
        ips=[line.split(',')[0] for line in f]
        return ips
    else:
        ips = [line.split()[0] for line in f]
        return ips

r=get_ips('log_report.txt','r')
print(r)