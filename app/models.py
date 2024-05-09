from app import db
from werkzeug.security import generate_password_hash, check_password_hash

# class Role(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(20), nullable=False, default='user')
    # role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    # role = db.relationship('Role', backref=db.backref('users', lazy='dynamic'))
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def is_active(self):
        # Assuming all users are active (you can implement custom logic if needed)
        return True
    
    def get_id(self):
        # Return the user ID as a string
        return str(self.id)
    def is_authenticated(self):
        # Check if the user is authenticated (logged in)
        return True  # Modify based on your authentication logic