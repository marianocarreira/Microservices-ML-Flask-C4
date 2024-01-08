#!/bin/sh
flask db init
flask db upgrade
python app.py