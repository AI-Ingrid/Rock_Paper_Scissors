import random
from statistics import mode


class Player:

    def __init__(self):
        self.name = "The player has no name yet"
        self.score = 0
        self.action_options = {
            "rock": "paper",
            "scissors": "rock",
            "paper": "scissors"}
        self.list_prev_actions = []
        self.list_opponent_prev_actions = []

    def select_action(self):
        pass

    def receive_result(self, score, action, opponent_action):
        self.score = score
        self.list_prev_actions.append(action)
        self.list_opponent_prev_actions.append(opponent_action)
        print("List of opponents prev actions: " + str(self.list_opponent_prev_actions))

    def enter_name(self):
        self.name = input("Enter you name: ")
        return self.name

    def get_random_action(self):
        return random.choice(list(self.action_options.keys()))


class RandomPlayer(Player):

    def __init__(self):
        super().__init__()

    def select_action(self):
        #print("RandomPlayer: The random action taken is: " + random_action)
        return self.get_random_action()


class SequentialPlayer(Player):
    def __init__(self):
        super().__init__()
        self.prev_action = ""

    def select_action(self):
        # first turn
        if self.prev_action == "":
            current_action = self.get_random_action()
            # print("Sequential Player: This was the first time. The action is: " +current_action)

        # not first time
        else:
            new_index = list(
                self.action_options.keys()).index(
                self.prev_action)
            if new_index == 2:
                new_index = 0
            else:
                new_index += 1

            current_action = list(self.action_options.keys())[new_index]
            # print("Sequential Player: Not the first time. The action chosen is: " + current_action)

        self.prev_action = current_action
        return current_action


class MostCommonPlayer(Player):
    def __init__(self):
        super().__init__()

    def select_action(self):
        # first turn
        if not self.list_opponent_prev_actions:
            current_action = self.get_random_action()
            # print("Most Common Player: This was the first time. The action is: " + current_action)

        else:
            current_action = self.action_options[(
                mode(self.list_opponent_prev_actions))]
            # print("Most Common Player: Not the first time. The most common action is: " + mode(self.list_opponent_prev_actions) +" The action is: " +current_action)
        return current_action


class HistorianPlayer(Player):
    def __init__(self, remember):
        super().__init__()
        self.length_sub_sequence = remember

    def select_action(self):
        # handling possible errors
        if self.length_sub_sequence > len(self.list_opponent_prev_actions) - 1:
            print("The number of actions you want to remember is longer "
                  "than the opponents previous actions. Action will therefore be random")
            current_action = self.get_random_action()
            return current_action

        # creating a list with the wanted sequence
        elif self.length_sub_sequence >= 1:
            length = len(self.list_opponent_prev_actions)
            current_sequence = []
            for i in range(length - self.length_sub_sequence, length):
                current_sequence.append(self.list_opponent_prev_actions[i])

            print(
                "The sequence we are gonna look for is: " +
                str(current_sequence))
            action_after_sub_sequence = []

            for j in range(0, length - 1):
                if self.list_opponent_prev_actions[j:j + len(
                        current_sequence)] == current_sequence and j != length - self.length_sub_sequence:
                    action_after_sub_sequence.append(
                        self.list_opponent_prev_actions[j + len(current_sequence)])
                else:
                    # the wanted sequence has not ben played before
                    current_action = self.get_random_action()
                    return current_action

            current_action = self.action_options[
                (mode(action_after_sub_sequence))]
            print(
                "Historian Player: List of Actions After Sub Sequence: " +
                str(action_after_sub_sequence))
            print("Historian Player: Current action taken: " + current_action)
            return current_action

        # handling an empty opponents prev action list
        elif not self.list_opponent_prev_actions:
            current_action = self.get_random_action()
            return current_action
