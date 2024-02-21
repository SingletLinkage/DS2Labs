# Question 3:
# Consider a well-shuffled deck of n cards, labelled 1 through n. You flip over the cards one
# by one, saying the numbers 1 through n as you do so. You win the game if, at some point, the number
# you say aloud is the same as the number on the card being flipped over (for example, if the 7th card in
# the deck has the label 7). What is the probability of winning? What should be the strategy for choosing
# n to maximize your win probability? Show the same using appropriate visualizations. Take n ≥ 2

import random
import matplotlib.pyplot as plt
import numpy as np
from itertools import permutations

N_LIMIT = 20
TEST_CASES = 80000  # must be more than 1000 for an accurate approximation

def simulate_test_case(n):
    cards = list(range(1, n + 1))
    random.shuffle(cards)
    win = False
    for i in range(n):
        if cards[i] == i + 1:
            win = True
            break
    return win

def calculate_actual_probab(n):
    # please do not run for higher values of n
    # time complexity: O(n!)
    all_cases = list(permutations(range(n)))
    wins = 0
    for case in all_cases:
        if any(case[i] == i for i in range(n)):
            wins += 1
    return wins/len(all_cases)


def main():
    # Simulating the game for different values of n
    n = 2
    probabilities = []
    actual = []
    while n <= N_LIMIT:
        simulation = [simulate_test_case(n) for _ in range(TEST_CASES)]
        simulated_win_probability = simulation.count(True) / TEST_CASES

        if n < 10: 
            # To prevent calling actual probability for large values of n
            actual_win_probability = calculate_actual_probab(n)
            print(f'Win probability for {n=} is {simulated_win_probability:.3f} ... actual: {actual_win_probability:.3f}')
            actual.append(actual_win_probability)
        else:
            print(f'Win probability for {n=} is {simulated_win_probability:.3f}')

        probabilities.append(simulated_win_probability)
        n += 1

    # getting some special values:
    max_prob = max(probabilities)
    max_prob_index = probabilities.index(max_prob) + 2

    min_prob = min(probabilities)
    min_prob_index = probabilities.index(min_prob) + 2

    print(f'Maximum win probability is {max_prob:.3f} for {max_prob_index=}')
    print(f'Minimum win probability is {min_prob:.3f} for {min_prob_index=}')

    # ================================ COSMETICS =================================
    plt.scatter([max_prob_index, min_prob_index], [max_prob, min_prob], color=['green', 'red'])
    plt.plot([min_prob_index, min_prob_index, 1], [0.45, min_prob, min_prob], linestyle='--', color='red')
    plt.plot([max_prob_index, max_prob_index, 1], [0.45, max_prob, max_prob], linestyle='--', color='green')
    plt.text(x=min_prob_index, y=min_prob, s=f'({min_prob_index}, {min_prob:.3f})', fontsize=8, color='k')
    plt.text(x=max_prob_index, y=max_prob, s=f'({max_prob_index}, {max_prob:.3f})', fontsize=8, color='k')

    plt.xlabel('Number of cards')
    plt.ylabel('Win probability')
    plt.yticks(np.arange(0.45, 0.7, 0.02))
    plt.xticks(np.arange(1, N_LIMIT + 1, 1, dtype=int))
    plt.grid(True)
    plt.title('Win probability vs Number of cards')
    # =============================== END COSMETICS ===============================

    plt.plot(range(2, N_LIMIT + 1), probabilities)
    plt.plot(range(2, len(actual)+2), actual, linestyle='--', color='black')
    plt.show()   


    # RESULT AFTER REPEATED TRIALS:
    print('Best strategy to win is to choose n=3; it has the highest win probability in range 0.66 to 0.67')
    print('Also: n = 2 has the lowest win chance of 0.5, while for larger values of n, the probability seems to have averaged out nearly in the 0.63-0.64 range')
    print('These inferences are based on observations of n from 2 upto 200')


if __name__ == '__main__':
    main()