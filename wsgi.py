import click, pytest, sys
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.main import create_app
from App.controllers import (
    create_user, get_all_users_json, get_all_users, initialize,
    create_driver, create_street, schedule_drive, list_drives,
    request_stop, update_driver_status
)

app = create_app()
migrate = get_migrate(app)

@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database initialized')

'''
BreadVan CLI Commands
'''
bread_cli = AppGroup('bread', help='BreadVan commands')

@bread_cli.command("seed-data", help="Seeds demo drivers and streets")
def seed_data():
    create_driver("John")
    create_driver("Sarah")
    create_street("Main Street")
    create_street("High Street")
    click.echo("Seed data added!")

@bread_cli.command("schedule-drive")
@click.option("--driver-id", required=True, type=int)
@click.option("--street-id", required=True, type=int)
@click.option("--time", required=True)
def schedule_drive_command(driver_id, street_id, time):
    d = schedule_drive(driver_id, street_id, time)
    click.echo(f"Drive {d.id} scheduled on street {street_id} at {time}")

@bread_cli.command("inbox")
@click.option("--street-id", required=True, type=int)
def inbox_command(street_id):
    drives = list_drives(street_id)
    for d in drives:
        click.echo(f"Drive {d.id}: Status={d.status}, Scheduled={d.scheduled_at}")

@bread_cli.command("request-stop")
@click.option("--drive-id", required=True, type=int)
@click.option("--resident", required=True)
@click.option("--note", default="")
def req_stop_command(drive_id, resident, note):
    s = request_stop(drive_id, resident, note)
    click.echo(f"Stop requested by {s.resident_name} for drive {drive_id}")

@bread_cli.command("driver-status")
@click.option("--drive-id", required=True, type=int)
@click.option("--status", required=True)
@click.option("--location", required=True)
def driver_status_command(drive_id, status, location):
    d = update_driver_status(drive_id, status, location)
    if d:
        click.echo(f"Drive {drive_id} updated: {status} at {location}")
    else:
        click.echo("Drive not found!")

app.cli.add_command(bread_cli)
