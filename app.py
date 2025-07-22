"""Main application file to run flask server"""

from flask import Flask
from routes import bp_routes
from models import db
from cli import create_tables, drop_tables, seed_data, update_data

# Initialise app as Flask object
app = Flask(__name__)

# Configure app with database details
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg2://jordan:wasd@localhost:5432/codecademy_flask_db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Since we're importing the db instance from models.py, we need to connect the
# app object to the db instance, allowing flask to talk to the database
db.init_app(app)

# Registers our routes through blueprints so we can access them
app.register_blueprint(bp_routes)

# Creates instance of cli commands so we can run them
app.cli.add_command(create_tables)
app.cli.add_command(drop_tables)
app.cli.add_command(seed_data)
app.cli.add_command(update_data)
