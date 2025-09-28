![Tests](https://github.com/uwidcit/flaskmvc/actions/workflows/dev.yml/badge.svg)

# Bread Van App
A Flask + SQLAlchemy application for managing bread delivery drives, drivers, streets, and resident stop requests.  
Includes a CLI interface for database initialization, user management, scheduling drives, and handling stop requests.



# Database Management
flask init           
*(Initialize and seed the database with demo data)*


# User Management
flask user create [username] [password]   
*(Create a new user (defaults: rob/robpass))*

flask user list [format]                  
*(List all users (format: string or json))*


# Bread Van Management
flask bread seed-data                      
*(Add demo drivers and streets)*


flask bread schedule-drive --driver-id=ID --street-id=ID --time="TIME"
*(Driver and route management)*

flask bread inbox --street-id=ID          
*(View scheduled drives for a street)*

flask bread request-stop --drive-id=ID --resident="NAME" --note="MESSAGE"
flask bread driver-status --drive-id=ID --status="STATUS" --location="LOCATION"
*(Stop requests and driver updates)*


# Testing
flask test user              
*(Run all user tests)*

flask test user unit         
*(Run only unit tests)*

flask test user int          
*(Run only integration tests)*


# Example Usage
flask init
*(Initialize the database)*

flask user create alice alicepass
flask user create bob bobpass
*(Create some users)*

flask bread seed-data
*(Add demo bread van data)*

flask bread schedule-drive --driver-id=1 --street-id=1 --time="2024-01-15 09:00"
*(Schedule a bread van drive)*

flask bread inbox --street-id=1
*(Check what drives are scheduled for a street)*

flask bread request-stop --drive-id=1 --resident="John Smith" --note="Need whole wheat bread"
*(Resident requests a stop)*

flask bread driver-status --drive-id=1 --status="EN_ROUTE" --location="Main St and 1st Ave"
*(Driver updates their status)*

flask test user
*(Run tests to verify everything works)*