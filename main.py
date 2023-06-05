import flask, logging, os

app = flask.Flask(__name__)
app.secret_key = os.urandom(32)

app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True

def generate_csrf():
    return os.urandom(16).hex()

@app.route('/')
def index():

    return '<h1>Index</h1>'

@app.route('/login', methods=['GET'])
def get_login():

    csrf = generate_csrf()
    flask.session['csrf-token'] = csrf

    return flask.render_template('login.html', csrf=csrf)

@app.route('/login', methods=['POST'])
def post_login():

    username = flask.request.form.get('username')
    password = flask.request.form.get('password')
    post_csrf = flask.request.form.get('csrf-token')
    
    if (session_csrf := flask.session.get('csrf-token')) == None:
        print('invalid csrf')
        return flask.make_response('<h1>Login failed</h1>', 401)

    if not username or not password:
        return flask.make_response('No username or password entered', 401)

    if post_csrf != session_csrf:
        return flask.make_response('<h1>Login failed</h1>', 401)

    print(username, password, post_csrf)

    if username == 'admin' and password == '11223344':
        print('login success')
        return flask.make_response('<h1>Login Success</h1>')
    
    return flask.make_response('<h1>Login failed</h1>', 401)

app.run(host='0.0.0.0', debug=False, threaded=True)
