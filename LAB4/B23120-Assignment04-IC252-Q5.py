import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# Uniform RV generation: X ~ Uniform(0, 1) and Y ~ Uniform(1, 2)
X = uniform(0, 1)
Y = uniform(1, 2)


def part_a():
    # Joint probability distribution
    x = np.linspace(0, 1, 100)
    y = np.linspace(1, 2, 100)

    joint_pdf = np.zeros((100, 100))  # Generate a 100 x 100 mesh for joint pdf
    for i in range(100):
        for j in range(100):
            joint_pdf[i, j] = X.pdf(x[i]) * Y.pdf(y[j])

    plt.imshow(joint_pdf, cmap='hot', interpolation='nearest')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xticks(np.linspace(0,1,10))
    plt.yticks(np.linspace(0,1,10))

    plt.title('Joint Probability Distribution')
    plt.colorbar()

    plt.show()


def part_b():
    # Checking for independence
    x = np.linspace(0, 1, 100)
    y = np.linspace(1, 2, 100)
    flag = True

    for i in range(100):
        for j in range(100):
            if X.pdf(x[i]) * Y.pdf(y[j]) != X.pdf(x[i]) * Y.pdf(y[j]):
                print('Not Independent')
                flag = False
                break

    if flag: print('Independent')


def part_c():
    # Required: P(X > 0.5 | Y = 1.5)
    # Since X and Y are independent, P(X > 0.5 | Y = 1.5) = P(X > 0.5) = 1 - P(X <= 0.5) = 1 - F(0.5)

    req_p = 1 - X.cdf(0.5)
    print('P(X > 0.5 | Y = 1.5) =', req_p)

def part_d():
    # P(X|Y = 1.5) = ?
    # P(X|Y = 1.5) = P(X = x | Y = 1.5) = P(X = x, Y = 1.5) / P(Y = 1.5)
    #              = P(X = x) * P(Y = 1.5) / P(Y = 1.5)
    #              = P(X = x)
    x = np.linspace(-1, 2, 100)
    cond_pdf = X.pdf(x)

    plt.plot(x, cond_pdf)
    plt.xlabel('X')
    plt.ylabel('P(X|Y = 1.5)')
    plt.title('Conditional Probability Distribution of X given Y = 1.5')
    plt.show()

def part_e():
    # Z = X + Y
    z = np.linspace(0, 4, 400)
    pdf = []
    for i in z:
        # z[i] = x + y
        # P(Z = z[i]) = P(X + Y = z[i]) = P(X = x) * P(Y = y) = P(X = z[i] - y) * P(Y = y)
        pdf.append(np.sum([X.pdf(i - y) * Y.pdf(y) for y in np.linspace(1, 2, 100)])/50)

    plt.plot(z, pdf)
    plt.xlabel('Z')
    plt.ylabel('PDF')
    plt.title('PDF of Z = X + Y')
    plt.show()
    
def part_f():
    # Generating random samples of Z = X + Y
    x_samples = np.random.uniform(0, 1, 100000)
    y_samples = np.random.uniform(1, 2, 100000)
    z_samples = x_samples + y_samples

    # plotting histogram of Z
    plt.hist(z_samples, bins=100, density=True)
    plt.xlabel('Z')
    plt.ylabel('Frequency')
    plt.title('Histogram of Z = X + Y')
    plt.show()

def main():
    part_a()
    part_b()
    part_c()
    part_d()
    part_e()
    part_f()


if __name__ == '__main__':
    main()