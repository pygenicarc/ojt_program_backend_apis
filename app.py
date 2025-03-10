from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy


todo = Flask(__name__)
todo.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db = SQLAlchemy(todo)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(100), nullable=False)
    task_desc = db.Column(db.String(1000), nullable=False)
    task_due = db.Column(db.String(50), nullable=False)


with todo.app_context():
    db.create_all()


@todo.route('/', methods=['GET'])
def get_all_tasks():
    data = Todo.query.all() # select * from Todo
    context = []
    for dt in data:
        db_data = {
            'id': dt.id,
            'task_name': dt.task_name,
            'task_desc': dt.task_desc,
            'task_due': dt.task_due
        }
        context.append(db_data) # [{},{},{},{},{}]
    print(f"data: {data}")
    return jsonify(context)


@todo.route('/submit', methods=['POST'])
def create_todo():
    data = request.get_json()
    print(f"data: {data}")
    # insert into Todo values('name', 'desc', 'due')
    new_task = Todo(task_name=data['task_name'], task_desc=data['task_desc'], task_due=data['task_desc'])
    db.session.add(new_task)
    db.session.commit()
    print(f"new_task: {new_task}")
    return jsonify({"message":"data added successfully !!!"})


@todo.route('/get-data')
def get_data():
    import requests

    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


@todo.route('/delete/<int:id>', methods=['GET', 'DELETE'])
def delete_task(id):
    task = Todo.query.get_or_404(id)

    if not task:
        return jsonify({'message': 'task not found'}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"message":"data delete successfully !!!"})


@todo.route('/get/<int:id>', methods=['GET'])
def get_task_by_id(id):
    task = Todo.query.get_or_404(id)

    if not task:
        return jsonify({'message': 'not found'}), 404

    return jsonify({
        "id":task.id,
        "task_name": task.task_name,
        "task_desc": task.task_desc,
        "task_due": task.task_due
    })


@todo.route('/update/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    task = Todo.query.get_or_404(id)

    if not task:
        return jsonify({'message': 'task not found'}), 404
    #
    #
    #
    #
    # db.session.update(task)
    # db.session.commit()
    return jsonify({"message":"data update successfully !!!"})


# I need host, port
if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5005,
        debug=True
    )
