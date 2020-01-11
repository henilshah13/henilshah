import bottle
#how to create website
app=bottle.Bottle()
@app.error(404)
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

@app.route('/verify',method='post')
def verifypage():
    u=bottle.request.forms.get('uname')
    p=bottle.request.forms.get('pw')
    if not (u=='abc' and p=='xyz'):
        return 'login failed'
    else:
        return 'login successful'

#app.run()
app.run(host='192.168.3.107',port=8080)