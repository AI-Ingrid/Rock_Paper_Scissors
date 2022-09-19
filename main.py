from players import *
from Tournament import Tournament


def main():
    """" Creating players """
    #random_player = RandomPlayer()
    #sequential_player = SequentialPlayer()
    most_common_player = MostCommonPlayer()
    #historian_player_1 = HistorianPlayer(1)
    historian_player_2 = HistorianPlayer(2)
    #historian_player_3 = HistorianPlayer(3)

    """
    # Playing a single game
    single_game_1 = SingleGame(random_player, sequential_player)
    single_game_1.perform_game()
    single_game_1.show_result()
    """

    """ Playing a tournament """
    tournament_1 = Tournament(historian_player_2, most_common_player, 100)
    tournament_1.arrange_tournament()


main()



