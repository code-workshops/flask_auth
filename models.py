from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __repr__(self):
        return f"<User {self.id} | {self.name}>"

    def save(self):
        db.session.add(self)
        db.session.commit()
        print(f"User {self.id} saved")

    def create_password(self, password):
        self.password = generate_password_hash(password)

    def is_valid_password(self, password):
        return check_password_hash(self.password, password)

    def change_password(self, password):
        if self.is_valid_password(password):
            self.create_password(password)
            self.save()


def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/flask_auth"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    # Used only to connect to app database.
    app = Flask(__name__)
    connect_to_db(app)
    db.create_all()
