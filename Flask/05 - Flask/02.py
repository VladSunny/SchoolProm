from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/hello')
@app.route('/first_page')
def first_page():
    return """<h1>Hello!</h1>
    <h4>It is our first page!</h4>
    <p>Made in L2SH!</p>"""


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")