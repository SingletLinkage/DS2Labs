import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

num_students = 50
X = np.array([2, 11, 23, 9, 4, 1])

# part a:
def part_a():
    pdf = X/np.sum(X)
    cdf = np.cumsum(pdf)
    # print(pdf, cdf)
    x_pts = np.arange(0, 6)
    plt.step(x_pts, cdf, color='blue', label='CDF')
    plt.step(x_pts, pdf, color='red', label='PDF')

    plt.xlabel('Values of X: ')
    plt.ylabel('Probability: ')

    plt.legend()
    plt.show()

def part_b():
    # pdf = reduce(lambda x, y: x + y, [X[i]*[i] for i in range(len(X))])
    # print(pdf)
    n_vals = [50, 500, 5000]

    headers = ['Number of Students', 'Average', 'Standard Deviation']
    data = []

    # ************* THEORETICAL *********************
    theory_val_avg = sum([i*X[i] for i in range(len(X))])/sum(X)
    theory_val_std = (sum([i*i*X[i] for i in range(len(X))])/sum(X) - theory_val_avg**2)**0.5  
    data.append([f'Theoretical Values', theory_val_avg, round(theory_val_std, 3)])
    # print(f'Theoretical values: avg: {theory_val_avg} and std dev: {theory_val_std:.3f}')

    # ************** SIMULATED **********************
    for n in n_vals:
        outcomes = np.random.choice([0, 1, 2, 3, 4, 5], size=n, p=X/sum(X), replace=True)
        lies_avg = 0
        lies_std = 0
        for i in outcomes:
            lies_avg += i
            lies_std += i**2
        lies_avg /= n
        lies_std = (lies_std/n - lies_avg**2)**0.5
        # print(f'Practical Value for {n=:<5} is: \n\taverage: {lies_avg:.3f} and \n\tstandard deviation: {lies_std:.3f}')
        data.append([n, round(lies_avg, 3), round(lies_std, 3)])

    table = tabulate(data, headers, tablefmt='grid')
    print(table)

def part_c():
    n = 50
    trials = 10000
    means = []
    for i in range(trials):
        outcomes = np.random.choice([0, 1, 2, 3, 4, 5], size=n, replace=True, p=X/sum(X))
        means.append(sum(outcomes)/n)
    plt.hist(means, bins=70)
    plt.show()  # appears to be a normal distro with some outliers

    # mean and variance of means:
    mean_m = np.mean(means)
    variance_m = np.var(means)

    print(f'Mean of the means: {mean_m:.3f}')
    print(f'Variance of the means: {variance_m:.3f}')


if __name__ == "__main__":
    part_a()
    part_b()
    part_c()