# Question 1:
# Suppose there are k people in a room. Assume each person’s birthday is equally likely to be
# any of the 365 days of the year (we exclude February 29), and that people’s birthdays are independent.
# What is the probability that at least one pair of people in the group have the same birthday? Plot the
# graph of the same as K grows from 2 to 100

import matplotlib.pyplot as plt
import numpy as np

def birthday_paradox(k):
    return 1 - np.prod((365 - np.arange(k)) / 365)

def birthday_paradox_other(k):
    value = 1
    for i in range(1, k+1):
        value = value * (365 - i + 1) / 365
    return 1 - value

k = np.arange(2, 101)
p = np.array([birthday_paradox(i) for i in k])

# ============================== COSMETICS ====================================
colors=['orange', 'green', 'cyan', 'magenta', 'yellow', 'red', 'blue', 'black']

# defining some special values:
values = [0.25, 0.5, 0.75, 0.999]

# setting up corresponding x and y points
x_pts = [np.where(p >= i)[0][0]+2 for i in values]
y_pts = [p[i-2] for i in x_pts]

# getting x and y limits
x_lim = plt.xlim()
y_lim = plt.ylim()

# scatter plot to show data points corresponding to the special values
plt.scatter(x_pts, y_pts, color=colors[:len(values)], s=30)

for i in range(len(values)):
    # plotting lines for better visualization
    plt.plot([x_pts[i], x_pts[i], x_lim[0]], [x_lim[0], y_pts[i], y_pts[i]], linestyle='--', color=colors[i])

    # adding text to the special values
    plt.text(x_pts[i], y_pts[i], f'({x_pts[i]}, {round(y_pts[i], 2)})', fontsize=10)

# setting up x and y labels, title, ticks and grid
plt.xlabel('Number of people in the room')
plt.ylabel('Probability of at least two of people having the same birthday')
plt.title('Birthday Paradox')
plt.xticks(np.arange(0, 101, 20))
plt.grid(True)
# ============================== END COSMETICS ====================================


# actual birthday paradox plot
plt.plot(k, p, color='r', linewidth=2)

plt.show()

