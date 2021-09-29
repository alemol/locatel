# -*- coding: utf-8 -*-
#
# Created by Alex Molina
# sept 2021
# 
# The code is licensed under the MIT License - see the LICENSE file for details.
# Copyright (c) 2021 Alejandro Molina Villegas

from application import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="localhost")