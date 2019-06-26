from flask import Flask

import os

app = Flask(__name__)

from app.controllers import login, register



