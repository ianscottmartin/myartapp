# seed.py

from app import app, db
from models import User, Artist, Museum, Review

# Initialize the app with the config
app.config.from_object("config.Config")

# Create tables in the database
db.create_all()


# Seed your database with initial data if needed
def seed_data():
    # Example: Create a user
    user = User(username="admin")
    user.set_password("password")
    db.session.add(user)

    # Add more seed data as needed

    db.session.commit()


if __name__ == "__main__":
    seed_data()
