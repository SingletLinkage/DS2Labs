# Question 2
# Stirling’s formula is given below is used to approximate the factorial of a given number.
#                               n! ~ √(2πn) * (n/e)^n
# Write a program to plot the ratio given below as n grows from 1 to 20.
#                               n! / (√(2πn) * (n/e)^n)

import math
import matplotlib.pyplot as plt
import numpy as np

def stirling_approx(n):
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == '__main__':
    n = np.arange(1, 21)
    p = np.array([factorial(i) / stirling_approx(i) for i in n])

    plt.plot(n, p, color='g', linewidth=2)
    plt.grid(True)
    plt.xticks(np.arange(1, 21, 1))
    plt.yticks(np.arange(1, 1.1, 0.01))
    plt.title('Ratio of n! to Stirling\'s Approximation')
    plt.xlabel('n', fontdict={'fontsize': 12})
    plt.ylabel('n! / Stirling\'s Approximation', fontdict={'fontsize': 12})
    plt.gcf().canvas.manager.set_window_title('Ratio of n! to Stirling\'s Approximation')
    plt.show()