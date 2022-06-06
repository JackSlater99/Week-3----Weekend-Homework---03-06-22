from flask import render_template, request
from app import app
from models.game import Game


@app.route('/')
def index():
    return render_template('index.html', title='Home - ')

@app.route('/game')
def game_index():
    return render_template('game.html', title='Rock, Paper, Scissors - ')

@app.route('/game', methods=["POST"])
def play_game_index():
    player_1_choice = request.form['player_1_choice']
    player_2_choice = request.form['player_2_choice']
    winner = Game.rock_paper_scissors(player_1_choice, player_2_choice)
    return render_template('game.html', title='Rock, Paper, Scissors - ', winner=winner)

@app.route('/game2')
def game2_index():
    return render_template('game2.html', title='Game 2 - ')

@app.route('/game3')
def game3_index():
    return render_template('game3.html', title='Game 3 - ')