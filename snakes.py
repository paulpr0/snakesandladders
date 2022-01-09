from random import randint
import statistics
import matplotlib.pyplot as plt
import random

def get_snakes_and_ladders():
    snakes = [
        (96,27),
        (88,66),
        (89,46),
        (79,44),
        (76,19),
        (74,52),
        (57,3),
        (60,39),
        (52,17),
        (50,7),
        (32,15),
        (30,9)
    ]
    ladders = [
        (6,28),
        (10,12),
        (18,37),
        (40,42),
        (49,67),
        (55,92),
        (63,76),
        (61,81),
        (86,94)
    ]
    return snakes + ladders

class SnakeOrLadder:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

class Game:

    def __init__(self) -> None:
        self.token = 1
        snakes_and_ladders_list = get_snakes_and_ladders()
        self.sl = {}
        for entry in snakes_and_ladders_list:
            self.sl[entry[0]] = entry[1]

    def move(self, howmany):
        self.token += howmany
        while (self.token in self.sl):
            self.token = self.sl[self.token]
        return self.token

    def turn(self):
        num = self.roll()
        self.move(num)
        if num == 6:
            self.turn()
        if self.token>=100:
            return True
        return False

    def roll(self):
        return randint(1,6)

def multiplayer_mins_and_maxes(results, number_of_players):
    mins = []
    maxes = []
    for i in range(1, int(len(results)/2)):
        sample = random.sample(results, number_of_players)
        mins.append(min(sample))
        maxes.append(max(sample))
    return (mins, maxes)

def chart_colours():
    pr0_blue = '#2E4BEE'
    pr0_orange = '#F09C54'

    pr0_yellow = '#F9BF4B'
    pr0_green1 = '#90A94B'
    pr0_green2 = '#3E8D6E'

if __name__ == '__main__':

    some_games = []
    for i in range(1,5):
        g = Game()
        board_positions = []
        while not g.turn():
            board_positions.append(g.token)
        board_positions.append(100)
        some_games.append(board_positions)
    for y in some_games:
        plt.plot(y)
    plt.title("Some Games")
    plt.show()

    results = []
    for i in range(1,10000):
        g = Game()
        turns = 0
        while not g.turn():
            turns +=1
        results.append(turns)

    print("min "+ str(min(results)))
    print("max "+ str(max(results)))
    print("mean "+ str(statistics.mean(results)))
    print("median " + str(statistics.median(results)))

    # samples for 2,3,4 players
    (min2, max2) = multiplayer_mins_and_maxes(results, 2)
    print(f"median for 2 players: min:{statistics.median(min2)}, max:{statistics.median(max2)}")
    (min3, max3) = multiplayer_mins_and_maxes(results, 3)
    print(f"median for 3 players: min:{statistics.median(min3)}, max:{statistics.median(max3)}")
    (min4, max4) = multiplayer_mins_and_maxes(results, 4)
    print(f"median for 4 players: min:{statistics.median(min4)}, max:{statistics.median(max4)}")


    fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=True)
    fig.set_figwidth(10)

    axs[0].hist(results, bins=10, range=(1,200))
    axs[0].set_title("One Player")
    axs[1].hist(min3, bins=10, range=(1,200))
    axs[1].set_title("3 Players, first to finish")
    axs[2].hist(max3, bins=10, range=(1,500))
    axs[2].set_title("3 Players, last to finish")

    plt.show()
