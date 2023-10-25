from dotenv import load_dotenv
from flask import Flask

load_dotenv()

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost/bracelet'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://doadmin:AVNS_XFw9y9FNVBcbqa0FjRh@db-postgresql-tor1-48594-do-user-14980657-0.c.db.ondigitalocean.com:25060/bracelet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking modifications for better performance

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)
