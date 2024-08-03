from flask import Flask

app = Flask(__name__, instance_relative_config=True)  # not too important to understand


app.config.from_object("config")  # get settings from config.py

from app import translate
from app import views
