from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/hello')

def first_page():
    return render_template("base.html")


@app.route('/second_page')
def second_page():
    return render_template("07.html")

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")