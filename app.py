from bottle import Bottle, template, request

app = Bottle()

@app.route('/')
def index():
    return template('views/index.html', name='', email='', message='', submitted=False)

@app.route('/', method='POST')
def submit_form():
    name = request.forms.get('name')
    email = request.forms.get('email')
    message = request.forms.get('message')
    return template('views/index.html', name=name, email=email, message=message, submitted=True)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
