from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('database.config')
db = SQLAlchemy(app)

from database.model import models