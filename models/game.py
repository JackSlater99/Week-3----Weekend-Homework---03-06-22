class Game():  
    def rock_paper_scissors(player_1, player_2):
        if player_1 == player_2:
            return ("Both Players selected the same choice, it's a draw!")
        elif player_1 == "rock":
            if player_2 == "scissors":
                return("Player 1 wins, rock brakes scissors!")
            else:
                return("Player 2 wins, paper covers rock!")
        elif player_1 == "paper":
            if player_2 == "rock":
                return("Player 1 wins, paper covers rock!")
            else:
                return("Player 2 wins, scissors cuts paper!")
        elif player_1 == "scissors":
            if player_2 == "paper":
                return("Player 1 wins, scissors cuts paper!")
            else:
                return("Player 2 wins, rock brakes scissors!")

        
