from flask_login import UserMixin

from app_config import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    user_id = db.Column('id', db.Integer, primary_key=True)
    login = db.Column('login', db.Text)
    password = db.Column('password', db.Text)

    def get_id(self):
        return self.user_id

