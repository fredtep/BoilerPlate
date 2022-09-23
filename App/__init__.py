import os
from flask import Flask, render_template
from importlib import import_module

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.DebugConfig')

@app.route('/')
def home():
    return render_template(
        'home.html',
        title="Flask Super Simple BoilerPlate",
        description="description"
        )