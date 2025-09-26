from App.database import db

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    drives = db.relationship('Drive', backref='driver', lazy=True)

    def __init__(self, name):
        self.name = name

    def get_json(self):
        return {"id": self.id, "name": self.name}

class Street(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    drives = db.relationship('Drive', backref='street', lazy=True)

    def __init__(self, name):
        self.name = name

    def get_json(self):
        return {"id": self.id, "name": self.name}

class Drive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)
    street_id = db.Column(db.Integer, db.ForeignKey('street.id'), nullable=False)
    scheduled_at = db.Column(db.String(50), nullable=False)  # store datetime as string for simplicity
    status = db.Column(db.String(20), default="SCHEDULED")  # could be SCHEDULED, EN_ROUTE, DONE
    location_text = db.Column(db.String(100), default="")

    stop_requests = db.relationship('StopRequest', backref='drive', lazy=True)

    def __init__(self, driver_id, street_id, scheduled_at):
        self.driver_id = driver_id
        self.street_id = street_id
        self.scheduled_at = scheduled_at

    def get_json(self):
        return {
            "id": self.id,
            "driver_id": self.driver_id,
            "street_id": self.street_id,
            "scheduled_at": self.scheduled_at,
            "status": self.status,
            "location_text": self.location_text
        }

class StopRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drive_id = db.Column(db.Integer, db.ForeignKey('drive.id'), nullable=False)
    resident_name = db.Column(db.String(50), nullable=False)
    note = db.Column(db.String(200), default="")
    status = db.Column(db.String(20), default="REQUESTED")  # REQUESTED, SERVICED

    def __init__(self, drive_id, resident_name, note=""):
        self.drive_id = drive_id
        self.resident_name = resident_name
        self.note = note

    def get_json(self):
        return {
            "id": self.id,
            "drive_id": self.drive_id,
            "resident_name": self.resident_name,
            "note": self.note,
            "status": self.status
        }
