import random

class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2


    def play_game(self, player1_choice, player2_choice):
        
        
        if player1_choice == player2_choice:
            return "It's a draw"

        elif player1_choice== "rock" and player2_choice== "paper":
            return "Player 2 wins playing paper over player's 1 rock"
        elif player1_choice== "rock" and player2_choice== "scissors":
            return "Player 1 wins playing rock over player's 2 scissors"
        
        elif player1_choice== "paper" and player2_choice== "scissors":
            return "Player 2 wins playing scissors over player's 1 paper"
        elif player1_choice== "paper" and player2_choice== "rock":
            return "Player 1 wins playing paper over player's 2 rock"
        
        elif player1_choice== "scissors" and player2_choice== "paper":
            return "Player 1 wins playing scissors over player's 2 paper"
        elif player1_choice== "scissors" and player2_choice== "rock":
            return "Player 2 wins playing rock over player's 1 scissors"
        
        else:
            return None

    def computer_picks(self):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        return computer_choice
