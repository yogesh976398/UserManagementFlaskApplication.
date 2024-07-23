from flask import Flask, request, jsonify
from models import User, Task
from schemas import UserSchema, TaskSchema
from database import db
from sqlalchemy.exc import IntegrityError
from flask_marshmallow import Marshmallow
from flask_cors import CORS

user_schema = UserSchema()
users_schema = UserSchema(many=True)
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


def create_app():
    app = Flask(__name__)
    CORS(app, origins='http://localhost:3000')
    # Initialize Marshmallow
    ma = Marshmallow(app)
    app.config.from_object('config.Config')
    db.init_app(app)
    ma.init_app(app)

    @app.before_request
    def create_tables():
        db.create_all()

    @app.route('/users', methods=['GET'])
    def get_users():
        users = User.query.all()
        return users_schema.jsonify(users)

    @app.route('/users', methods=['POST'])
    def add_user():
        username = request.json.get('username')
        email = request.json.get('email')
        if not username or not email:
            return jsonify({'error': 'Invalid input'}), 400
        new_user = User(username=username, email=email)
        try:
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'User already exists'}), 400
        return user_schema.jsonify(new_user), 201

    @app.route('/users/<int:id>', methods=['GET'])
    def get_user(id):
        user = User.query.get_or_404(id)
        return user_schema.jsonify(user)

    @app.route('/users/<int:id>', methods=['PUT'])
    def update_user(id):
        user = User.query.get_or_404(id)
        username = request.json.get('username')
        email = request.json.get('email')
        if username:
            user.username = username
        if email:
            user.email = email
        db.session.commit()
        return user_schema.jsonify(user)

    @app.route('/users/<int:id>', methods=['DELETE'])
    def delete_user(id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        tasks = Task.query.all()
        return tasks_schema.jsonify(tasks)

    @app.route('/tasks', methods=['POST'])
    def add_task():
        title = request.json.get('title')
        description = request.json.get('description')
        due_date = request.json.get('due_date')
        user_id = request.json.get('user_id')
        if not title or not user_id:
            return jsonify({'error': 'Invalid input'}), 400
        new_task = Task(title=title, description=description, due_date=due_date, user_id=user_id)
        db.session.add(new_task)
        db.session.commit()
        return task_schema.jsonify(new_task), 201

    @app.route('/tasks/<int:id>', methods=['GET'])
    def get_task(id):
        task = Task.query.get_or_404(id)
        return task_schema.jsonify(task)

    @app.route('/tasks/<int:id>', methods=['PUT'])
    def update_task(id):
        task = Task.query.get_or_404(id)
        title = request.json.get('title')
        description = request.json.get('description')
        due_date = request.json.get('due_date')
        if title:
            task.title = title
        if description:
            task.description = description
        if due_date:
            task.due_date = due_date
        db.session.commit()
        return task_schema.jsonify(task)

    @app.route('/tasks/<int:id>', methods=['DELETE'])
    def delete_task(id):
        task = Task.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return '', 204

    return app
