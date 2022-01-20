from bottle import get, post, run, request # or route

@get('/login') # or @route('/login')
def submit():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/submit') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('hostNameSection')
    print(username)

run(host='localhost', port=8080, debug=True)