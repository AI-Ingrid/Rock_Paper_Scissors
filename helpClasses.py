""" Help classes """


class Action:
    def __init__(self, action):
        self.action = action
        print("Playing " + action)
        self.win_loose_actions = {
            "rock": ["scissors", "rock", "paper"],
            "paper": ["rock", "paper", "scissors"],
            "scissors": ["paper", "scissors", "rock"]}
        self.action_hierarchy = self.win_loose_actions[self.action]

    def __eq__(self, other):
        if self.action == other.action:
            print(self.action + " against " + other.action)
            return True
        return False

    def __gt__(self, other):
        if self.action_hierarchy.index(self.action) > self.action_hierarchy.index(other.action) \
                and not self.__eq__(other):
            print(self.action + " beats " + other.action)
            return True

        print(other.action + " beats " + self.action)
        return False


class SingleGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.name_player1 = ""
        self.name_player2 = ""

        self.choice_player1 = ""
        self.choice_player2 = ""

        self.score_player1 = 0
        self.score_player2 = 0

        self.winner = ""

    def perform_game(self):
        if self.name_player1 == "":
            print("Let's play!")
            print("Player 1: ")
            self.name_player1 = str(self.player1.enter_name())
            print("Player 2: ")
            self.name_player2 = str(self.player2.enter_name())
            print("Welcome " + self.name_player1 + " and " + self.name_player2 + ". Let's play!")

        print(self.name_player1 + " is choosing")
        self.choice_player1 = self.player1.select_action()
        action_player1 = Action(self.choice_player1)

        print(self.name_player2 + " is choosing")
        self.choice_player2 = self.player2.select_action()
        action_player2 = Action(self.choice_player2)

        """ Checking who wins """
        if action_player1.__eq__(action_player2):
            self.score_player1 = 0.5
            self.score_player2 = 0.5

        else:
            if action_player1.__gt__(action_player2):
                self.score_player1 = 1
                self.score_player2 = 0
                self.winner = self.name_player1
            else:
                self.score_player2 = 1
                self.score_player1 = 0
                self.winner = self.name_player2

        """ Reporting the results back to the players """
        self.player1.receive_result(self.score_player1, self.choice_player1, self.choice_player2)
        self.player2.receive_result(self.score_player2, self.choice_player2, self.choice_player1)

    def show_result(self):
        print(self.name_player1 + " chose " + self.choice_player1 + " while " +
              self.name_player2 + " chose " + self.choice_player2)

        if self.winner != "":
            print(self.winner + " won!")

        else:
            print("It's a draw!")

    def get_scores(self):
        return self.score_player1, self.score_player2
