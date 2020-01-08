import sqlite3
con=sqlite3.connect('mydb.sqlite3')

#import pymysql
#con = pymysql.connect(user='',password='',host='',port='',datadbase='')

cur=con.cursor()
query='''create table if not exists logdata(
            id varchar(100),
            date varchar(100),
            pics varchar(100),
            url varchar(100))'''
cur.execute(query)

import urllib.request as u
myurl='https://www.jafsoft.com/searchengines/log_sample.html'
f=u.urlopen(myurl)

import re
for line in f:
    #print(line)
    #print(type(line))
    line=line.decode()
    #print(type(line))
    m=re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*',line)
    if m !=None:
        ip=m.group(1)
        print(ip)
        print(line)