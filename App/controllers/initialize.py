from .user import create_user
from App.database import db
from App.controllers import create_driver, create_street

def initialize():
    # Reset database
    db.drop_all()
    db.create_all()

    # Create default admin/test user
    create_user('bob', 'bobpass')

    # Automatically seed demo data for Bread Van
    create_driver("John")
    create_driver("Sarah")
    create_street("Main Street")
    create_street("High Street")

    print("Database initialized with demo users, drivers, and streets!")
