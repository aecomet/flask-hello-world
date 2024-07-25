from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! This is a Flask app served with Gunicorn, using gunicorn/main.py."

@app.route('/foo')
def foo():
    return "bar/hoge"

if __name__ == '__main__':
    app.run()

