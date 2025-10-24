from flask import Flask, render_template

app = Flask(__name__)

names = 'Вася Коля Петя'.split()


@app.route('/<name>')
def student(name):
    if name in names:
        return f"<h1>Hello, { name }!</h1>"
    return f"Такой страницы не существует"


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")