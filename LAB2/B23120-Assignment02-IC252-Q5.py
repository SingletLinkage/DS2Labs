# Question 5:
# Develop a Python program to simulate the Monty Hall problem, a probability puzzle inspired by a game show scenario.

# (a) Simulate a scenario where a contestant is presented with three closed doors.
# (b) Behind one door is a valuable prize, while the other two doors conceal worthless items.
# (c) Initially, the contestant selects one door (without it being opened).
# (d) The game show host, who knows what is behind each door, then opens one of the other two doors that doesn’t contain the prize.
# (e) The contestant is given the option to stick with their original choice or switch to the other un-opened door.
# (f) Repeat the experiment for a specified number of trials (e.g., 10,000 trials).
# (g) Record whether the contestant wins the prize or not for each trial, based on their final decision (stick or switch).
# (h) Calculate the probability of winning the prize when the contestant sticks with their initial choice and when they switch doors.
# (i) Display the results and probability distributions in a clear and organized format.

import random
import matplotlib.pyplot as plt

door_items = [0, 0, 1]  # 0 for worthless items, 1 for valuable prize
switch_choice = [0, 1]  # 0 for stick with initial choice, 1 for switch to other un-opened door
TRIALS = 10000
outcomes = [[0,0],[0,0]]  # [ stick:[loss, win], switch:[loss, win] ]

def simulate(doors: list, initial: int, switch: int) -> int:  # 0 for loss, 1 for win
    return switch ^ doors[initial]

def print_stats(stats: list) -> None:
    print(''.center(50, '='))
    print('Monty Hall Problem Simulation Results:')
    print(''.center(50, '='))
    print('Stats when player did not switch doors:')
    print(f'Loss: {stats[0][0]}  ||\tWin: {stats[0][1]}')
    print(f'Probability of winning: {stats[0][1]/sum(stats[0]):.2f}')
    print(''.center(50, '='))
    print('Stats when player switched doors:')
    print(f'Loss: {stats[1][0]}  ||\tWin: {stats[1][1]}')
    print(f'Probability of winning: {stats[1][1]/sum(stats[1]):.2f}')
    print(''.center(50, '='))


def main():
    for i in range(TRIALS):
        random.shuffle(door_items)
        door_choice = random.randint(0, len(door_items)-1)
        switch = random.choice(switch_choice)
        outcomes[switch][simulate(door_items, door_choice, switch)] += 1

    print_stats(outcomes)
    probabilities = [[outcomes[0][0]/sum(outcomes[0]), outcomes[0][1]/sum(outcomes[0])], 
                     [outcomes[1][0]/sum(outcomes[1]), outcomes[1][1]/sum(outcomes[1])]]

    plt.subplot(1, 2, 1)
    plt.title('Stick with initial choice')
    plt.bar(['Loss', 'Win'], probabilities[0], color=['red', 'green'])
    plt.yticks([i/10 for i in range(0, 11)])
    plt.ylabel('Probability', fontdict={'fontsize': 12})
    plt.grid(True)
    plt.gca().set_axisbelow(True)

    plt.subplot(1, 2, 2)
    plt.tick_params(
        axis='y',
        which='both',
        left=False,
        labelleft=False
    )
    plt.title('Switch to other door')
    plt.bar(['Loss', 'Win'], probabilities[1], color=['red', 'green'])
    plt.yticks([i/10 for i in range(0, 11)])
    plt.grid(True)
    plt.gca().set_axisbelow(True)
    
    plt.figtext(0.53, 0.02, 'Outcomes', ha='center', va='center', fontdict={'fontsize': 12})  
    plt.suptitle('Monty Hall Problem Simulation Results', fontsize=15)
    plt.tight_layout()
    plt.gcf().canvas.manager.set_window_title('Monty Hall Problem Simulation Results')
    plt.show()    


if __name__ == "__main__":
    main()