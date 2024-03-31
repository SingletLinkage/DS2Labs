import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import NormalDist

# Exam Marks - normal distribution
# prof A : mean: 78, std: 5
# prof B : mean: 85, std: 3

# exam difficulty probab: 
# easy - 0.3
# moderate - 0.5
# hard - 0.2

# Setting up datasets
prof_a = NormalDist(mu=78, sigma=5)
prof_b = NormalDist(mu=85, sigma=3)
difficulty_probab = {
    'easy': 0.3,
    'moderate': 0.5,
    'hard': 0.2
}

def P_getting_score(score):
    # P (X) : P(getting score X)
    p_prof_a = prof_a.pdf(score)
    p_prof_b = prof_b.pdf(score)
    return np.array((p_prof_a, p_prof_b, (p_prof_a + p_prof_b)/2))

def join_probab(score, difficulty):
    # P (X, Y) : P(getting score X along difficulty Y)
    return P_getting_score(score) * difficulty_probab[difficulty]

def part_a():
    # loop across all scores from 0 to 100 - checking probab of each along 3 difficulty levels
    scores = np.arange(0, 100, 0.01)
    pdf = {
        'easy': [],
        'moderate': [],
        'hard': []
    }

    for score in scores:
        for difficulty in difficulty_probab:
            pdf[difficulty].append(join_probab(score, difficulty)[-1])
    
    # plotting
    plt.plot(scores, pdf['easy'], label='easy')
    plt.plot(scores, pdf['moderate'], label='moderate')
    plt.plot(scores, pdf['hard'], label='hard')

    plt.xlabel('Score')
    plt.ylabel('Probability')
    plt.title('Probability distribution of scores')
    plt.legend()
    plt.show()

    return pd.DataFrame(pdf, index=scores)

def part_b(df: pd.DataFrame):
    marginal_score = df.sum(axis=1)
    marginal_difficulty = df.sum(axis=0) / df.count() * 100

    # plotting
    _, ax = plt.subplots(1, 2)
    ax[0].plot(marginal_score, label='Score')
    ax[1].bar(df.columns, marginal_difficulty, label='Difficulty')

    ax[0].set_xlabel('Score')
    ax[0].set_ylabel('Probability')
    ax[0].set_title('Marginal distribution of scores')

    ax[1].set_xlabel('Difficulty')
    ax[1].set_ylabel('Probability')
    ax[1].set_title('Marginal distribution of difficulty')

    plt.show()

def part_c():
    # P(X > 80 | Y = easy) = P(X > 80, Y = easy) / P(Y = easy)
    #                      = P(X > 80) * P(Y = easy) / P(Y = easy)
    #                      = P(X > 80)
    print(f'{1 - (prof_a.cdf(80) + prof_b.cdf(80))/2:.3f}')

def part_d():
    scores = np.arange(0, 100, 0.01)
    p_a = []
    p_b = []
    p_tot = []
    for score in scores:
        a, b, t = P_getting_score(score)
        p_a.append(a)
        p_b.append(b)
        p_tot.append(t*2)
    
    # plotting
    plt.plot(scores, p_a, label='prof A')
    plt.plot(scores, p_b, label='prof B')
    plt.plot(scores, p_tot, label='Total')

    plt.xlabel('Score')
    plt.ylabel('Probability')
    plt.title('Probability distribution of scores')
    plt.legend()
    plt.show()

def part_e():
    # If professors are more likely to assign harder exams to students with higher expected scores, the score normal distribution would even out slightly as the actual marks of students having a higher expected score will get diminished as a consequence of getting a harder paper while the actual marks of students having a lower expecxted score will increase as theyll get a easier paper. The standard deviation and variance of marks will decrease but mean will remain the same. The height of the peak will increase as the marks of all students will approach the mean marks.
    ...


def main():
    df = part_a()
    part_b(df)
    part_c()
    part_d()


if __name__ == '__main__':
    main()