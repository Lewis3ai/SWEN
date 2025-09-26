from App.models import db, Driver, Street, Drive, StopRequest

def create_driver(name):
    new_driver = Driver(name=name)
    db.session.add(new_driver)
    db.session.commit()
    return new_driver

def create_street(name):
    new_street = Street(name=name)
    db.session.add(new_street)
    db.session.commit()
    return new_street

def schedule_drive(driver_id, street_id, time):
    new_drive = Drive(driver_id=driver_id, street_id=street_id, scheduled_at=time)
    db.session.add(new_drive)
    db.session.commit()
    return new_drive

def list_drives(street_id):
    return Drive.query.filter_by(street_id=street_id).all()

def request_stop(drive_id, resident_name, note=""):
    new_stop = StopRequest(drive_id=drive_id, resident_name=resident_name, note=note)
    db.session.add(new_stop)
    db.session.commit()
    return new_stop

def update_driver_status(drive_id, status, location_text):
    drive = Drive.query.get(drive_id)
    if not drive:
        return None
    drive.status = status
    drive.location_text = location_text
    db.session.commit()
    return drive
