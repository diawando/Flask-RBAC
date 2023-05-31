from flask_security import UserMixin, RoleMixin
from app import db


# create table in database for assigning roles
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

# create table in database for storing users
class User (db.Model, UserMixin):
    __tablename__= 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean())
    # backreferences the user_id from roles_users table
    roles = db.relationship('Role', secondary=roles_users, backref='roled')
    

# create table in database for storing roles
class Role(db.Model, RoleMixin)
    __tablename__ = 'role'
    id = db.Column (db.Integer(), primary_key=True)
    name = db.Column (db.String(80), unique=True)
    
