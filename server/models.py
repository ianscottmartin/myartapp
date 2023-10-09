# models.py

from app import db
import bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        # Hash the password and store it in the database
        self.password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    def check_password(self, password):
        # Verify if the provided password matches the stored hashed password
        return bcrypt.checkpw(
            password.encode("utf-8"), self.password_hash.encode("utf-8")
        )


class Artist(db.Model):
    # Define artist model fields
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String, unique=True)
    work = db.Column(db.String, unique=True)


class Museum(db.Model):
    # Define museum model fields
    id = db.Column(db.Integer, primary_key=True)
    museum = db.Column(db.String, unique=True)
    city = db.Column(db.String, unique=True)


class Review(db.Model):
    # Define review model fields
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String, unique=True)
