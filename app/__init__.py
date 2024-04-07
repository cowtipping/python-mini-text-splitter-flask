from flask import Flask

app = Flask(__name__)

from app import routes  # It's at the end of the file to avoid circular imports.
