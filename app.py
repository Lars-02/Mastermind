#!/usr/bin/env python
import os

from flask import Flask, render_template, request, redirect, url_for, abort, flash

from model.color import Color
from model.game import Game
from model.game_create_form import GameCreateForm
from model.guess import Guess

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')
app.jinja_env.filters['zip'] = zip
app.jinja_env.filters['enumerate'] = enumerate
app.jinja_env.filters['color'] = Color

games = [Game("Game 1", 10, 4, 12, False)]


@app.route('/')
def home():
    return render_template('index.html', games=games)


@app.route('/stats')
def stats():
    return render_template('stats.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
    form = GameCreateForm(request.form)
    if request.method == 'POST' and form.validate():
        new_game = Game(form.name.data, form.guesses.data,
                        form.positions.data, form.colors.data, form.double_colors.data)
        games.append(new_game)
        flash('Game created')
        return redirect(url_for('game', game_id=len(games)))
    return render_template('create.html', form=form)


@app.route('/game/<int:game_id>')
def game(game_id):
    if game_id < 0 or game_id > len(games) - 1:
        abort(404)
    return render_template('game.html', game=games[game_id], game_id=game_id)


@app.route('/game/<int:game_id>/guess', methods=['POST'])
def submit_guess(game_id):
    games[game_id - 1].add_guess(Guess(tuple(Color(int(n)) for n in list(request.form.values()))))
    return redirect(url_for('game', game_id=game_id))


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
