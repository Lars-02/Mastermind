#!/usr/bin/env python
from model import Game
import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')

game = Game(10, 4, 6, False)


@app.route('/')
def home():
    return render_template('home.html', game=game)


# 404 error handler
@app.errorhandler(404)
def page_not_found(_):
    return render_template('errors/404.html'), 404


# 500 error handler
@app.errorhandler(500)
def internal_server_error(_):
    return render_template('errors/500.html'), 500


if (__name__ == "__main__"):
    app.run(debug=True)
