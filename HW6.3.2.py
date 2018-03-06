from enum import Enum
import numpy as np
import scr.FigureSupport as Fig
import scr.StatisticalClasses as Stat


class CoinToss(Enum):  # State of each coin toss
    HEADS = 1
    TAILS = 0


class Game:  # create cointoss game
    def __init__(self):
        self._rnd = np.random  # generate random number for coin flip
        self._headProb = head_prob  # probability of getting Heads
        self._CoinToss = []  # outcome of toss
        self._results = []  # outcome of all tosses in a Game

    def simulate(self, tosses):
        t = 0  # first toss
        while t < tosses:  # while number of tosses has not been reached
            if self._rnd.sample() < self._headProb:  # odds of getting heads
                self._CoinToss = CoinToss.HEADS
            else:
                self._CoinToss = CoinToss.TAILS  # if not heads, then tails
            self._results.append(self._CoinToss.name)  # create list of results
            t += 1  # repeat toss
            # print (t) #to check number of tosses

    def tally1(self):
        countable = " ".join(map(str, self._results))
        wins = countable.count(winning_sequence)
        total = -entry_fee + (wins * reward)
        # print (countable) # TO CHECK for number of tosses
        # print (wins) # TO CHECK number of tosses
        # print (total) # TO CHECK total
        return total

    def tally2(self):
        if self.tally1() < 0:
            loss = 1
        else:
            loss = 0
        return loss


class Rounds:
    def __init__(self, rounds):
        self.initialRounds = rounds
        self.games = []
        self.losses =[]
        self.total_tally1 = []
        self.total_tally2 = []

        for i in range(rounds):  # to iterate through rounds
            game = Game()  # game is an instance of Game
            self.games.append(game)  # create a list of games to append the talliies
            self.losses.append(game)

    def play(self):
        for game in self.games:
            game.simulate(n_tosses)  # initiate cointoss
            outcome = game.tally1()
            outcome2 = game.tally2()
            self.total_tally1.append(outcome)
            self.total_tally2.append(outcome2)

    def get_total_tally1(self):  # creates a list of the value of each round
        return self.total_tally1

    def get_total_tally2 (self):
        return self.total_tally2

    def get_avg_tally(self):  # returns the average value
        self.summary_stats1 = Stat.SummaryStat("Expected Value",self.get_total_tally1())
        return self.summary_stats1.get_mean()

    def get_avg_tally2(self):  # returns the average value
        self.summary_stats2 = Stat.SummaryStat("Loss",self.get_total_tally2())
        return self.summary_stats2.get_mean()

    def get_expected_value_CI(self,alpha):
        return self.summary_stats1.get_t_CI(alpha)

    def get_expected_value_PI(self,alpha):
        return self.summary_stats1.get_PI(alpha)

    def get_expected_loss_CI(self,alpha):
        return self.summary_stats2.get_t_CI(alpha)

    def get_expected_loss_PI(self,alpha):
        return self.summary_stats2.get_PI(alpha)

    def get_min_tally(self):  # returns the minimum value
        return min(self.total_tally1)

    def get_max_tally(self):  # returns the maximum value
        return max(self.total_tally1)


# Values of constants
head_prob = 0.5
n_tosses = 20
num_rounds = 10
entry_fee = 250
reward = 100
winning_sequence = "TAILS TAILS HEADS"
ALPHA = 0.05

myRounds = Rounds(num_rounds)  # Create rounds
myRounds.play()  # Play rounds



print("Expected value:", myRounds.get_avg_tally())
print("95% PI:", myRounds.get_expected_value_PI(ALPHA))
print()
print("Probability of loss:", myRounds.get_avg_tally2())
print("95% PI:", myRounds.get_expected_loss_PI(ALPHA))
print()
print ("The gambler is analyzed as a transient-state simulation model,")
print ("as there are only 10 observations, such that the Law of Large Numbers")
print ("can not be applied to make any inferences about the sample mean.")
print("We are therefore more interested in the distribution of our expected value and probability of losss.")
print()
print ("Consequently, we use the prediction interval, which can be interpreted as:")
print ("The next realization of the expected value")
print ("will fall in the projection interval", myRounds.get_expected_value_PI(ALPHA))
print ("with probability 0.95.")
print()
print ("The next realization of the probability of loss")
print ("will fall in the projection interval", myRounds.get_expected_loss_PI(ALPHA))
print ("with probability 0.95.")
print()
print("Minimum value:", myRounds.get_min_tally())
print("Minimum possible value:", -entry_fee)
print("Maximum value:", myRounds.get_max_tally())
print("Maximum possible value: 350")
print()
print("Based on a coin toss game with the following parameters:")
print("Probability of getting Heads:", head_prob)
print("Number of coin tosses per game:", n_tosses)
print("Number of rounds of games:", num_rounds)
print("Entry fee to play each game:", entry_fee)
print("Reward for each winning sequence:", reward)
print("Alpha=",ALPHA)
print("Winning sequence:", winning_sequence)



# plot the histogram
Fig.graph_histogram(
    observations=myRounds.get_total_tally1(),
    title='Histogram of Rewards',
    x_label='Rewards ($)',
    y_label='Rounds')
