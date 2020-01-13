import flask
#how to create website
app=flask.Flask('myapp')

@app.errorhandler(404)
def errorpage(err):
    return 'page under construction'
@app.route('/')
def indexpage():
    return 'welcome'
@app.route('/about')
def aboutpage():
    return '<b>welcome to about</b>'
@app.route('/login')
def loginpage():
    return '''<form action='/verify' method='post'>
    username: <input type='text' name='uname'/></br>
    password: <input type='password' name='pw'/></br>
    <input type='submit' value='login'/>
    </form>'''

@app.route('/verify',methods=['post'])
def verifypage():
    u=flask.request.form.get('uname')
    p=flask.request.form.get('pw')
    if not (u=='abc' and p=='xyz'):
        return 'login failed'
    else:
        import sqlite3
        con=sqlite3.connect('mydb.sqlite3')
        cur=con.cursor()
        cur.execute('select * from logdata')
        result=cur.fetchall()
        return flask.render_template('report.html',res=result)

@app.route('/download/<filename>')
def staticfile(filename):
    return flask.send_from_directory(directory=r'C:\pythontraining\bin',filename=filename)

@app.route('/empid/<int:eid>')
def empid(eid):
    d={'name':'abc','EMP_ID':eid}
    return d

@app.route('/logdata')
def logdata():
    return flask.redirect('/login')

@app.route('/password')
def password():
    return flask.abort(201,'access denied')


#app.run()
app.run(host='192.168.3.107',port=8080)