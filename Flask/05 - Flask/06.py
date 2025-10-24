from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<name>')
def student(name):
    kwargs = {"student_name": name,
              "exam_mark": 2,
              "student_surname": "Примеров"}
    return render_template("student.html", **kwargs)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")