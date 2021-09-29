# -*- coding: utf-8 -*-
#
# Created by Alex Molina
# sept 2021
# 
# The code is licensed under the MIT License - see the LICENSE file for details.
# Copyright (c) 2021 Alejandro Molina Villegas
from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')

    with app.app_context():
        from application.routes import routes
        # register blueprints
        app.register_blueprint(routes.locatel)
        return app
