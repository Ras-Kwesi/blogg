from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Class for the table that manages users,
class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    age = db.Column(db.Integer)
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    pass_key = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    user_pitch = db.relationship('Pitches', backref='user', lazy='dynamic')


    def save_user(self):
        db.session.add(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_key = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_key, password)



class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(255))
    user_pitch = db.relationship('Comments', backref='blog', lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blog(cls, id):
        blog = Blog.query.filter_by(poster=id).all()
        return blog



class Mailer(db.Model):
    __tablename__ = 'mailers'
    id = db.Column(db.Integer, primary_key=True)
    emails = db.Column(db.String(255))
    name = db.Column(db.String(255))




    def save_mail(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_email(cls, id):
        email = Mailer.query.filter_by(poster=id).all()
        return email

class Comments(db.Model):
    __tablename__="comments"
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    blog_comment = db.Column(db.Integer, db.ForeignKey('blogs.id'))




    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments = Comments.query.filter_by(pitch_comment=id).all()
        return comments