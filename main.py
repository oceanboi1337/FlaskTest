import flask, logging

app = flask.Flask(__name__)

app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True

@app.route('/')
def index():

    return '<h1>Index</h1>'

@app.route('/login', methods=['GET'])
def get_login():

    return flask.send_file('index.html')

@app.route('/login', methods=['POST'])
def post_login():

    username = flask.request.form.get('username')
    password = flask.request.form.get('password')
    
    if username and password:

        if username == 'admin' and password == '11223344':

            return flask.make_response('<h1>Login Success</h1>')
        
    return flask.make_response('<h1>Login failed</h1>', 401)

app.run(host='0.0.0.0', debug=False, threaded=True)