from datetime import datetime
from app import db, login_manager
from flask import current_app
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id}, salt='password-reset-salt')

    @staticmethod
    def verify_reset_token(token, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token, salt='password-reset-salt', max_age=expires_sec)['user_id']
        except Exception:
            return None
        return User.query.get(user_id)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'image_file': self.image_file,
            'posts': [post.to_dict() for post in self.posts]
        }

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'date_posted': self.date_posted.isoformat(),
            'user_id': self.user_id,
            'author': self.author.username
        }

class Cube(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), default=None)
    cube_mainboard = db.Column(db.Text, nullable=False)
    cube_sideboard = db.Column(db.Text, nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'creator_id': self.creator_id,
            'name': self.name,
            'cube_mainboard': self.cube_mainboard,
            'cube_sideboard': self.cube_sideboard,
            'date_created': self.date_created
        }
class CardInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(101), unique=True, nullable=False)
    mana_cost = db.Column(db.String(25))
    type_line = db.Column(db.String(75))
    image = db.Column(db.String(256))

    def to_dict(self):
        return {
            'id': self.id,
            'card_name': self.card_name,
            'mana_cost': self.mana_cost,
            'type_line': self.type_line,
            'image': self.image,
        }

class ActiveCubeDecks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(101), db.ForeignKey('card_info.card_name'), unique=True, nullable=False)
    mana_cost = db.Column(db.String(25), db.ForeignKey('card_info.mana_cost'))
    type_line = db.Column(db.String(75), db.ForeignKey('card_info.type_line'))
    image = db.Column(db.String(256), db.ForeignKey('card_info.image'))
    card_id = db.Column(db.Integer, db.ForeignKey('card_info.id'), unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'card_name': self.card_name,
            'mana_cost': self.mana_cost,
            'type_line': self.type_line,
            'image': self.image,
            'card_id': self.card_id
        }
    
class Draft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'date_created': self.date_created.isoformat()
        }