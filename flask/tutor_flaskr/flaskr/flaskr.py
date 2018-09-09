import os
import sqlite3

from flask import (Flask, request, session, g, redirect, url_for, abort,
    render_template, flash)

# create the application instance
app = Flask(__name__) 

# Load config from this file
app.config.from_object(__name__) 

# Load default config and override config from an environment variable
app.config.update(
    DATABASE = os.path.join(app.root_path, "flaskr.db"),
    SECRET_KEY = b"_5#y2L\"F4Q8z\n\xec]/",
    USERNAME = "admin",
    PASSWORD = "default"
)
app.config.from_envvar("FLASKR_SETTINGS", silent=True)


def connect_db():
    rv = sqlite3.connect(app.config["DATABASE"])
    rv.row_factory = sqlite3.Row
    return rv




