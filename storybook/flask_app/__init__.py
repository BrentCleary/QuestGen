
# Import Flask from flask (must be installed in folder with "pipenv install flask")
# app is called in server.py to run flask server for routes
from flask import Flask
app = Flask(__name__)
app.secret_key = "secret"

# Key for API calls - Import into image controller
APIKEY = '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';
DATABASE = 'storybook_schema'

