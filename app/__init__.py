import json
from flask import Flask

app = Flask(__name__)

with open('.env.json') as config_file:
    config = json.load(config_file)

app.config['HOST'] = config['host']
app.config['PORT'] = config['port']
app.config['PASSWORD_MIN_LENGTH'] = config['password_min_length']
app.config['PASSWORD_MAX_LENGTH'] = config['password_max_length']

from app import routes
