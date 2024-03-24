import random
import matplotlib.pyplot as plt

class Player:
    def __init__(self, name, strategy):
        self.name = name
        self.round_score = 0
        self.score_sum = 0
        self.scores = []
        self.strategy = strategy
        self.actions = []  # Добавляем список действий соперника
        self.opponent_actions = []  # Добавляем список действий соперника

    def cooperate(self):
        return "cooperate"

    def betray(self):
        return "betray"

    def choose_action(self):
        return self.strategy.choose_action(self.actions, self.opponent_actions)

        # return self.strategy.choose_action(self.last_opponent_action)

    def get_score_sum(self):
        return self.score_sum

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play_round(self):
        action1 = self.player1.choose_action()
        action2 = self.player2.choose_action()

        if action1 == "cooperate" and action2 == "cooperate":
            self.player1.round_score = 3
            self.player2.round_score = 3
        elif action1 == "cooperate" and action2 == "betray":
            self.player1.round_score = 0
            self.player2.round_score = 5
        elif action1 == "betray" and action2 == "cooperate":
            self.player1.round_score = 5
            self.player2.round_score = 0
        else:
            self.player1.round_score = 1
            self.player2.round_score = 1

        self.player1.score_sum += self.player1.round_score
        self.player2.score_sum += self.player2.round_score
        self.player1.scores.append(self.player1.score_sum)
        self.player2.scores.append(self.player2.score_sum)

        self.player1.actions.append(action1)
        self.player1.opponent_actions.append(action2)
        self.player2.actions.append(action2)
        self.player2.opponent_actions.append(action1)
#удалить ниже

        print(f"Раунд: {len(self.player1.scores)}")
        print("очк 1 игрока вся сумма: ", self.player1.score_sum)
        print("очк 1 игрока сумма на текущий раунд: ", self.player1.scores[:])
        print(f"{self.player1.name} ({self.player1.strategy.name}) выбрал {action1} и получил {self.player1.round_score} очков.")
        print(f"{self.player2.name} ({self.player2.strategy.name}) выбрал {action2} и получил {self.player2.round_score} очков.")
        print(f"Очки {self.player1.name}: {self.player1.get_score_sum()}, очки {self.player2.name}: {self.player2.get_score_sum()}")

class Strategy:
    def __init__(self, name):
        self.name = name

    def choose_action(self, last_opponent_action):
        pass

class RandomStrategy(Strategy):
    def __init__(self):
        self.name = "random"
    def choose_action(self, player_actions, opponent_actions):
        return random.choice(["cooperate", "betray"])

class FriedmanStrategy(Strategy):
    """
    Класс Фридман, начинает с сотрудничества. Если предают 1 раз начинает предавать всегда
    
    Атрибуты:
    - name: имя игрока
    """
    def __init__(self):
        self.name = "Friedman"
    def choose_action(self, player_actions, opponent_actions):
        if opponent_actions[-1:] == "betray":
            return "betray"
        else:
            return "cooperate"

class JossStrategy(Strategy):
    def __init__(self):
        self.name = "Joss"
    def choose_action(self, player_actions, opponent_actions):
        if opponent_actions[-1:] == "betray" or random.random() < 0.1:
            return "betray"
        else:
            return "cooperate"

# player1 = Player("Игрок 1", RandomStrategy())
# player2 = Player("Игрок 2", RandomStrategy())
player1 = Player("Игрок 1", random.choice([RandomStrategy(), FriedmanStrategy(), JossStrategy()]))
player2 = Player("Игрок 2", random.choice([RandomStrategy(), FriedmanStrategy(), JossStrategy()]))
game = Game(player1, player2)

for _ in range(10):
    game.play_round()

print("Итоговые очки:")
print(f"Очки {player1.name}: {player1.get_score_sum()}, очки {player2.name}: {player2.get_score_sum()}")

plt.plot(player1.scores, label=f"{player1.name} ({player1.strategy.name})")
plt.plot(player2.scores, label=f"{player2.name} ({player2.strategy.name})")
plt.xlabel('Раунд')
plt.ylabel('Очки')
plt.legend()
plt.show()