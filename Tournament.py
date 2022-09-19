from matplotlib import pyplot as plt
from Rock_Paper_Scissors.helpClasses import SingleGame


class Tournament:
    def __init__(self, player1, player2, number_of_games):
        self.player1 = player1
        self.player2 = player2
        self.number_of_games = number_of_games

    def arrange_single_game(self):
        game = SingleGame(self.player1, self.player2)
        game.perform_game()
        game.show_result()

    def arrange_tournament(self):
        print(" ------ The tournament starts now! -------")
        score_player1 = []
        score_player2 = []
        win_per_player1 = 0
        win_per_player2 = 0
        prev_win_per_player1 = []
        prev_win_per_player2 = []

        tournament = SingleGame(self.player1, self.player2)

        for i in range(0, self.number_of_games):
            print("This is game: " + str(i+1) + "/" + str(self.number_of_games))

            """ Playing a game """
            tournament.perform_game()
            tournament.show_result()

            """ Saving scores from the game"""
            temp_score_player1, temp_score_player2 = tournament.get_scores()
            score_player1.append(temp_score_player1)
            score_player2.append(temp_score_player2)

            """ Calculating win percentage """
            win_per_player1 = sum(score_player1)/len(score_player1)*100
            win_per_player2 = sum(score_player2)/len(score_player1)*100

            """ Saving the win percentage in a list"""
            prev_win_per_player1.append(win_per_player1)
            prev_win_per_player2.append(win_per_player2)

        print("Score player 1: " + str(score_player1))
        print("Score player 2: " + str(score_player2))
        print("Win percentage player 1: " + str(win_per_player1) +
              ". Win percentage player 2: " + str(win_per_player2))

        """ Plotting the development of the win percentage for the players """
        x_axis = list(range(1, self.number_of_games+1, 1))
        plt.plot(x_axis, prev_win_per_player1, label=tournament.name_player1)
        plt.plot(x_axis, prev_win_per_player2, label=tournament.name_player2)
        plt.xlabel("Number of games played")
        plt.ylabel("Win percentage")
        plt.legend(loc="upper left")
        plt.show()
