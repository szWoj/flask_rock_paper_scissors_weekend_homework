from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player

@app.route('/<choice1>/<choice2>')
def the_game(choice1, choice2):
    player1 = Player("Mike", choice1)
    player2 = Player("Alex", choice2)
    game = Game(player1, player2)
    winner = game.play_game(choice1, choice2)
    return render_template("result.html", winner=winner)

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/play') #? methods=['GET']
def game_against_computer():
    player_choice = "paper" #request.form["choice_formm"]
    computer_choice = "rock" #game.computer_picks()
    game = Game("Mark", "Computer")
    
    winner_against_computer = game.play_game(player_choice, computer_choice)
    return render_template("play_computer.html", winner_against_computer = winner_against_computer)


# @app.route('/play')
# def game_against_computer(player_choice, computer_choice):
#     #player_choice = request.form["choice_form"]
#     player1 = Player("Mike", player_choice)
#     computer_player = Player("Computer", computer_choice)
#     game = Game(player1, computer_player)
#     #computer_choice = game.computer_game()
    
#     winner_against_computer = game.play_game(player_choice, computer_choice)
#     return render_template("play_computer.html", winner_against_computer = winner_against_computer)