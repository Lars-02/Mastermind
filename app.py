#!/usr/bin/env python
import os
import pickle

from flask import Flask, render_template, request, redirect, url_for, abort, flash, Response

from model.correct import Correct
from model.color import Color
from model.game import Game
from model.game_create_form import GameCreateForm
from model.guess import Guess

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')
app.jinja_env.filters['zip'] = zip
app.jinja_env.filters['enumerate'] = enumerate
app.jinja_env.filters['color'] = Color

if os.path.exists("games.pickle"):
    with open('games.pickle', 'rb') as file:
        games = pickle.load(file)
else:
    games = [Game("Game 1", 10, 4, 12, False)]


@app.context_processor
def inject_context():
    return dict(Correct=Correct)


@app.route('/')
def home():
    return render_template('index.html', games=games)


@app.route('/stats')
def stats():
    games_won = 0
    guesses = 0
    games_by_name = {}
    for g in games:
        if g.has_won():
            games_won += 1
        guesses += len(g.guesses)
        if g.nickname not in games_by_name:
            games_by_name[g.nickname] = []
        games_by_name[g.nickname].append(g)
    return render_template('stats.html', games=games, games_won=games_won, guesses=guesses, games_by_name=games_by_name)


@app.route('/create', methods=['GET', 'POST'])
def create():
    form = GameCreateForm(request.form)
    if request.method == 'POST' and form.validate():
        new_game = Game(form.name.data, form.guesses.data,
                        form.positions.data, form.colors.data, form.double_colors.data)
        games.append(new_game)
        flash('Game created')
        return redirect(url_for('game', game_id=len(games) - 1))
    return render_template('create.html', form=form)


@app.route('/game/<int:game_id>')
def game(game_id):
    if not 0 <= game_id < len(games):
        abort(404)
    return render_template('game.html', game=games[game_id], game_id=game_id)


@app.route('/game/<int:game_id>/guess', methods=['POST'])
def submit_guess(game_id):
    if not 0 <= game_id < len(games):
        abort(404)
    if (not games[game_id].has_won()) or (not games[game_id].has_lost):
        games[game_id].add_guess(Guess(tuple(Color(int(n))
                                             for n in list(request.form.values()))))
    return redirect(url_for('game', game_id=game_id))


@app.route('/game/<int:game_id>/cheat')
def cheat(game_id):
    if not 0 <= game_id < len(games):
        abort(404)

    if (not games[game_id].has_won()) or (not games[game_id].has_lost):
        games[game_id].cheated = True

    return redirect(url_for('game', game_id=game_id))


@app.route('/save')
def save():
    with open('games.pickle', 'wb') as file:
        pickle.dump(games, file, protocol=pickle.HIGHEST_PROTOCOL)
    return redirect(url_for('home'))


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
