from app_config import db


class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column('id', db.Integer, primary_key=True)
    login = db.Column('login', db.Text)
    password = db.Column('password', db.Text)
