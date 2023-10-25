from dotenv import load_dotenv
from flask import Flask

load_dotenv()

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost/bracelet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking modifications for better performance

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)
