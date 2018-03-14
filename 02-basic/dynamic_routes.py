from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/user/<str:username>')
def user(username):
    username = username # + 1
    return '<h1>Hello World, %s</h1>' % username


if __name__ == '__main__':
    app.run(debug=True)
