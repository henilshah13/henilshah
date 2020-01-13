#api-1 -> ip
#api1=http://127.0.0.1:8080/ip

import bottle
app=bottle.Bottle()
@app.route('/ip',method='GET')
def api_ip():
    import sqlite3
    con=sqlite3.connect('mydb.sqlite3')
    cur=con.cursor()
    cur.execute('select id from logdata')
    result=cur.fetchall()
    result=[i[0] for i in result]
    d={k:v for k,v in enumerate(result)}
    return d

#api2-http://127.0.0.1:8080/emp
@app.route('/emp',method='post')
def empdetails():
    details=bottle.request.params
    details=dict(details)
    return details

@app.route('/json')
def fromjson():
    f=open('mydata.json','w')
    d={"course":"python","loc":"blr"}
    import json
    json.dump(d,f)
    f.close()
    f=open('mydata.json')
    r=json.load(f)
    f.close()
    return r






app.run()