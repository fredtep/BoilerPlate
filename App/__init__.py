import os
from flask import Flask, render_template
from importlib import import_module

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.DebugConfig')

    # a simple page that says hello
    @app.route('/')
    def home():
        return render_template(
            'home.html',
            title="title",
            description="description"
            )

    return app