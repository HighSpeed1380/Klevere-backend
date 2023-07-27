from flask_sqlalchemy import SQLAlchemy
import enum
from datetime import datetime

db = SQLAlchemy()

class RoleType(enum.Enum):
    ADMIN = "A"
    USER = 'U'

class User(db.Model):

    """Model for users table"""
    __table_name__ = 'users'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    public_id = db.Column(db.String(255), unique = True, nullable=False, default="")
    name = db.Column(db.String(255), default="")
    company_name = db.Column(db.String(255), nullable=False, default="")
    email = db.Column(db.String(255), nullable=False, unique=True, default="")
    avatar = db.Column(db.String(255), default="")
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum(RoleType), default=RoleType.USER, nullable=False)
    status = db.Column(db.Boolean, default=1)
    email_verified_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now(), nullable=False, onupdate=datetime.now())

    @property
    def serialize(self):
        
        if self.role == RoleType.ADMIN:
            role = 'ADMIN'
        else:
            role = 'USER'
        return {
            'public_id': self.public_id,
            'name': self.name,
            'company_name': self.company_name,
            'email': self.email,
            'avatar': self.avatar,
            'role': role,
            'status': self.status,
            'email_verified_at': self.email_verified_at,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
    

class Test(db.Model):
    "Model for test table"
    __table_name__ = 'test'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)