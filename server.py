import random
from sqlalchemy import event
from datetime import datetime
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy
from data_structure.custom_q import Queue
from flask import Flask, request, jsonify
from data_structure.stack import Stack
from data_structure.hash_table import HashTable
from data_structure.linked_list import LinkedList
from sqlite3 import Connection as SQLite3Connection
from data_structure.binary_search_tree import BinarySearchTree


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 0


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0

# configure sqlite3 to enforce foreign key contraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


db = SQLAlchemy(app)
now = datetime.now()


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost", cascade="all, delete")

class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


@app.route('/user/', methods=['POST'])
def create_user():
    user = request.get_json()
    new_user = User(
        name = user['name'],
        email = user['email'],
        address = user['address'],
        phone = user['phone'],
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Created user Done"}), 200

@app.route('/user/descending_id/', methods=['GET'])
def get_all_user_descending():
    users = User.query.all()
    all_user_linked = LinkedList()
    for user in users:
        all_user_linked.insert_start(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "address": user.address,
                "phone": user.phone
            }
        )
    return jsonify(all_user_linked.to_list()), 200

@app.route('/user/ascending_id/', methods=['GET'])
def get_all_user_ascending():
    users = User.query.all()
    all_user_linked_list = LinkedList()
    for user in users:
        all_user_linked_list.insert_end({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone
        })
    return jsonify(all_user_linked_list.to_list()), 200

@app.route('/user/<user_id>/', methods=['GET'])
def get_one_user(user_id):
    users = User.query.all()
    all_user_linked_list = LinkedList()
    for user in users:
        all_user_linked_list.insert_start({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone
        })
    user = all_user_linked_list.get_user_by_id(user_id)
    return jsonify(user), 200

@app.route('/user/<user_id>/delete', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({
        "message": "done"
    }), 200

@app.route('/blog/<user_id>/create', methods=['POST'])
def create_blog_post(user_id):
    data = request.get_json()
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"Message": "User doen't exist"}), 400
    hashTable = HashTable(10)
    hashTable.add_key_value("title", data['title'])
    hashTable.add_key_value("body", data['body'])
    hashTable.add_key_value("date", now)
    hashTable.add_key_value("user_id", user_id)

    # hashTable.print_table()
    # print(hashTable.get_value('title'))
    # print(hashTable.get_value('body'))
    # print(hashTable.get_value('date'))
    # print(hashTable.get_value('user_id'))
    new_blog = BlogPost(
        title = hashTable.get_value('title'),
        body = hashTable.get_value('body'),
        date = hashTable.get_value('date'),
        user_id = hashTable.get_value('user_id')
    )    
    db.session.add(new_blog)
    db.session.commit()
    return jsonify({'message': "New blog post created"}), 200

@app.route('/blog/<blog_post_id>/all', methods=['GET'])
def get_one_blog_post(blog_post_id):
    blog_post = BlogPost.query.all()
    random.shuffle(blog_post)
    binarysearch = BinarySearchTree()

    for blog in blog_post:
        binarysearch.insert({
            "id": blog.id,
            'title': blog.title,
            "body": blog.body,
            "user_id": blog.user_id
        })

    post = binarysearch.search(blog_post_id)
    if not post:
        return jsonify({'message': "Post not found"}), 401
    return jsonify(post), 200


@app.route('/blog/numeric_bodies/', methods=['GET'])
def blog_post_numeric_bodies():
    blog_post = BlogPost.query.all()
    queue = Queue()
    for post in blog_post:
        queue.enqueue(post)

    return_list = list()
    for _ in range(len(blog_post)):
        post = queue.dequeue()
        numeric_body = 0
        for char in post.data.body:
            numeric_body += ord(char)
        post.data.body = numeric_body
        return_list.append({
            "id": post.data.id,
            "title": post.data.title,
            "body": post.data.body,
            "user_id": post.data.user_id
        })
    return jsonify(return_list), 200

@app.route('/blog/delete_last_10/', methods=['DELETE'])
def delete_last_10():
    blog_post = BlogPost.query.all()
    stack = Stack()
    for post in blog_post:
        stack.push(post)
    for _ in range(10):
        delete_post_to = stack.pop()
        db.session.delete(delete_post_to.data)
        db.session.commit()
    return jsonify({"message": "success"})


if __name__ == '__main__':
    app.run(debug=True)
