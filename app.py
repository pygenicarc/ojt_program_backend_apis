from flask import Flask, render_template, jsonify
import requests

todo = Flask(__name__)


@todo.route('/student-info')
def index():
    student = [
        {
            "name":"abc",
            "age": 10,
            "dept":"cse"
        },
        {
            "name": "edf",
            "age": 10,
            "dept": "cse"
        },
        {
            "name": "xyz",
            "age": 10,
            "dept": "ece"
        },
        {
            "name": "abc",
            "age": 10,
            "dept": "cse"
        },
        {
            "name": "edf",
            "age": 10,
            "dept": "cse"
        },
        {
            "name": "xyz",
            "age": 10,
            "dept": "ece"
        },
        {
            "name": "abc",
            "age": 10,
            "dept": "cse"
        },
        {
            "name": "edf",
            "age": 10,
            "dept": "cse"
        },
        {
            "name": "xyz",
            "age": 10,
            "dept": "ece"
        }
    ]
    return jsonify(student)
    # return render_template('student.html', data=student)


@todo.route('/get-student')
def get_student():
    url = "http://127.0.0.1:5005/student-info"

    payload = {}
    headers = {}

    response = requests.request("GET", url)

    return jsonify(response.json())


# I need host, port
if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5005,
        debug=True
    )
