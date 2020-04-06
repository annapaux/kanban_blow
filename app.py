from flask import render_template, url_for, flash, redirect, request,Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_api import FlaskAPI
import json


app = Flask(__name__)
api = FlaskAPI(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
db = SQLAlchemy(app)

#Todos Model
class Todos(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    todo_item = db.Column(db.String(500),  nullable=True)
    todo_date = db.Column(db.String(500), nullable=True)
    done = db.Column(db.Boolean, default=False)
    def __repr__(self):
        return f'Todo item {self.todo_item} due on {self.todo_date}'

db.create_all()

@app.route('/', methods=['GET', 'POST'])
def todo():
    todo_item = request.form.get('todo_item') or None
    todo_date = request.form.get('todo_date') or None
    new_item = Todos(todo_item = todo_item, todo_date=todo_date)
    if todo_item and todo_date:
        db.session.add(new_item)
        db.session.commit()
        flash(f"Todo item '{todo_item}' added, due '{todo_date}'",'success')

    all_todos = Todos.query.all()
    return render_template('todo.html', all_todos = all_todos)


@app.route('/delete_todo/<todo_id>', methods=['GET', 'POST'])
def delete_todo(todo_id):
    my_todo = Todos.query.get_or_404(todo_id)
    flash(f"Todo item {my_todo.todo_item} deleted",'info')
    db.session.delete(my_todo)
    db.session.commit()
    return redirect(url_for('todo'))

@app.route('/not_todo/<todo_id>', methods=['GET', 'POST'])
def not_todo(todo_id):
    my_todo = Todos.query.get_or_404(todo_id)
    my_todo.done = not my_todo.done
    db.session.add(my_todo)
    db.session.commit()
    flash(f"Todo item {my_todo.todo_item} is {'NOT' if not my_todo.done else ''} done", 'info')
    return redirect(url_for('todo'))

# A route to return available entries in our catalog.
@app.route('/api/v1/todos/<items>', methods=['GET', 'POST'])
def api(items):
    todo_items = {}
    if request.method == 'GET':
        if items == 'all':
            todos = Todos.query.all()
        else:
            try:
                items = int(items)
                todos = Todos.query.get_or_404(items)
            except:
                return {
                    'status':404,
                    'message':'Input valid parameter, either /api/v1/todos/all or /api/v1/todos/<todo_id>'
                }
        try:
            todos.done
            todos = [todos]
        except:
            pass
        for todo in todos:
            todo_items[todo.id] = {
                'todo_title': str(todo.todo_item),
                'todo_status': str(todo.done),
                'todo_due_date': str(todo.todo_date)
            }
    return jsonify(todo_items)



def validate(todos):
    for todo in todos:
        if todo['todo_due_date'] and todo['todo_title']:
            continue
        else:
            return False
    return True

@app.route('/api/v1/todos_add/', methods=['GET','POST'])
def add_items():
    todos = eval(request.args['items'])
    print('our todos',todos)
    if validate(todos):
        for todo in todos:
            new_todo = Todos(todo_item=todo['todo_title'], todo_date=todo['todo_due_date'])
            db.session.add(new_todo)
        db.session.commit()
        return jsonify({
            'status': 200,
            'message': f'{len(todos)} todo items added'
        })


    else:
        return jsonify({
            'status': 404,
            'message': 'Bad input, structure your Todo token correctly and ensure it has a title and due date.',
            'valid example': [
                {
                    'todo_due_date': '2020-04-15',
                    'todo_status': 'False',
                    'todo_title': 'Add new'
                }, ...
            ]
        })

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
    api.run(debug=True)
