def add():
    a = 10
    b = 20
    c = a + b
    print('c=', c)

add()
add()

def get_ips():
    f = open(r'C:\pythontraining\log\serverlog.txt')
    ips = [line.split()[0] for line in f if line[:3].isdigit()]
    print(ips)

get_ips()
print(ips)
