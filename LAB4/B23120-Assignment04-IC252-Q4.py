import matplotlib.pyplot as plt
import numpy as np
from statistics import NormalDist

# Details for AM:
#     Mean : 1hr
#     Std Dev: 0.5hr

# Details for FM:
#     Mean : 1.5hr
#     Std Dev: 0.75hr

# Simulation Capacity: 100 AM and 100 FM

# Setup the datasets for AM and FM
AM_pdf = NormalDist(mu=1, sigma=0.5)
FM_pdf = NormalDist(mu=1.5, sigma=0.75)


def part_0():
    #simulating stuff
    # Take samples
    am_vals = AM_pdf.samples(100)
    fm_vals = FM_pdf.samples(100)
    plt.scatter(am_vals, fm_vals) 
    plt.show()


def part_a():
    pts = 1000
    # Generate the random samples for AM and FM
    samples = np.linspace(0, 3, pts)

    X, Y = np.meshgrid(samples, samples)
    joint_pdf_values = np.zeros_like(X)
    for i in range(pts):
        for j in range(pts):
            joint_pdf_values[i, j] = AM_pdf.pdf(samples[i]) * FM_pdf.pdf(samples[j])

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, joint_pdf_values, cmap='coolwarm')
    ax.set_xlabel('AM')
    ax.set_ylabel('FM')
    ax.set_zlabel('Joint PDF')
    ax.set_title('Joint PDF Surface Plot')
    plt.show()


def part_b():
    # P(t_FM < 1 | t_AM = 2) = P(t_FM < 1) = F(t_FM = 1)
    p = FM_pdf.cdf(1)
    print(f'{p:.3f}')

def part_c():
    # T = t_FM + t_AM -> simulation for 100 pair of AM and FM
    pts = 1000
    # Generate the random samples for AM and FM
    samples = np.linspace(0, 3, pts)

    T = [AM_pdf.pdf(i) + FM_pdf.pdf(i) for i in samples]

    # Plot pdfs - line plot
    plt.plot(samples, T, label='Total Time')
    plt.legend()
    plt.title('Combined AM and FM Time PDF')

    plt.show()

def part_d():
    # mean and std dev of T
    pts = 1000
    # Generate the random samples for AM and FM
    samples = np.linspace(0, 3, pts)
    T = [AM_pdf.pdf(i) + FM_pdf.pdf(i) for i in samples]

    mean = np.mean(T)
    std_dev = np.std(T)

    print(f'Mean: {mean:.3f}, Std Dev: {std_dev:.3f}')


def part_e():
    # Y -> RV -> remaining repair time
    # pdf of Y ? for AM and FM separately
    # Assume X : repair time for a radio
    # Z : time taken for ongoing repair

    # Y = X - Z

    # For AM radios:
    # X ~ Normal(1, 0.5) and ZAM ~ Normal(1, 0.5)
    # YAM -> Normal(1, 0.5) - Normal(1, 0.5) = Normal(0, ((0.5)^2 + (0.5)^2)^0.5)

    # For FM radios:
    # X ~ Normal(1.5, 0.75) and ZFM ~ Normal(1.5, 0.75)
    # YFM -> Normal(1.5, 0.75) - Normal(1.5, 0.75) = Normal(0, ((0.75)^2 + (0.75)^2)^0.5)

    # Plot the PDFs
    samples = sorted(np.random.randint(0, 500, 10000)/100)
    YAM_pdf = NormalDist(mu=0, sigma=(0.5**2 + 0.5**2)**0.5)
    YFM_pdf = NormalDist(mu=0, sigma=(0.75**2 + 0.75**2)**0.5)

    # Plot pdfs - line plot
    plt.plot(samples, [YAM_pdf.pdf(i) for i in samples], label='YAM')
    plt.plot(samples, [YFM_pdf.pdf(i) for i in samples], label='YFM')

    plt.legend()
    plt.title('YAM and YFM PDFs')

    plt.show()

def main():
    part_0()
    part_a()
    part_b()
    part_c()
    part_d()
    part_e()

if __name__ == '__main__':
    main()