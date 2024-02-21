# Question 4:
# Develop a Python program to simulate the throwing of two dice and compute the 
# probability distribution of the sum of the numbers obtained on the two dice.
# 
# The program should perform the following tasks:
# (a) Calculate the sum of the numbers obtained on the two dice.
# (b) Repeat the process for a substantial number of trials (e.g., 10,000 trials).
# (c) Tabulate the frequency of each possible sum (2 through 12).
# (d) Compute the probability of each sum by dividing its frequency by the total number of trials.
# (e) Display the probability distribution of the sum of the numbers obtained on the two dice.

import random
import matplotlib.pyplot as plt

def get_random_dice_throw_sum():
    return random.randint(1,6) + random.randint(1,6)

TRIALS = 10000
possible_sums = range(2,13)
frequency = [0] * len(possible_sums)

def main():
    for i in range(TRIALS):
        sum = get_random_dice_throw_sum()
        frequency[sum-2] += 1

    probablity = [f/TRIALS for f in frequency]

    print('Sum\tFrequency\tProbability')
    for i in range(len(possible_sums)):
        print(f"{possible_sums[i]}\t{frequency[i]}\t\t{probablity[i]:.2f}")

    plt.grid(True)
    plt.gca().set_axisbelow(True)
    plt.bar(possible_sums, probablity)
    plt.xticks(possible_sums)
    plt.title('Probability Distribution of Sum of Numbers Obtained on the Two Dice')
    plt.gcf().canvas.manager.set_window_title('Probability Distribution of Sum of Numbers Obtained on the Two Dice')
    plt.xlabel('Sum of the Numbers obtained on dice throw', fontdict={'fontsize': 12})
    plt.ylabel('Probability', fontdict={'fontsize': 12})
    plt.show()

if __name__ == "__main__":
    main()