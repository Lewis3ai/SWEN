from .user import create_user
from App.database import db
from .breadvan import create_driver, create_street

def initialize():
    # Reset database
    db.drop_all()
    db.create_all()

    # Create streets first
    main_st = create_street("Main Street")
    high_st = create_street("High Street")

    # Create drivers
    create_driver("John")
    create_driver("Sarah")

    # Create users and assign them to streets
    bob = create_user('bob', 'bobpass')
    bob.street_id = main_st.id

    alice = create_user('alice', 'alicepass')
    alice.street_id = main_st.id

    charlie = create_user('charlie', 'charliepass')
    charlie.street_id = high_st.id

    db.session.commit()

    print("Database initialized with demo users, drivers, and streets!")
    print("Users: bob and alice on Main Street, charlie on High Street")
    