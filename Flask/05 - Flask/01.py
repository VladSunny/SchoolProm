from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/hello')
@app.route('/first_page')
def first_page():
    return "Hello! This is our first page!"


@app.route('/second_page')
def second_page():
    return "Hello! This is our second page!"


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")