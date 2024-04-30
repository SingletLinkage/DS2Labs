import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import tabulate as tb

def stats(sample):
    mean = np.mean(sample)
    std_dev = np.std(sample)
    return mean, std_dev

def plot(ax:plt.axes, sample, idx, n):
    ax.hist(sample, bins=30, density=True, alpha=0.3, label='Sample '+str(idx))
    ax.set_title(f'N= {n}')
    ax.set_ylabel('Frequency')


mean = 65
std_dev = 15

# initialise normal distro object:
norm_dist = norm(loc=mean, scale=std_dev)

# part a:
sample_size = 50
def part_a(sample_size, ax):
    samples = [norm_dist.rvs(size=sample_size) for i in range(5)]

    # plot actual:
    x = np.linspace(20, 120, 1000)
    ax.plot(x, norm_dist.pdf(x), 'k--', lw=2, label='Actual')

    headers = ['Sample_size', 'Sample', 'Mean', 'Std Dev']
    rows = []
    for i, sample in enumerate(samples):
        mean, std_dev = stats(sample)
        rows.append([sample_size, f'{i+1}', f'{mean:.3f}', f'{std_dev:.3f}'])
        plot(ax, sample, i+1, sample_size)
    
    print(tb.tabulate(rows, headers, tablefmt='grid'))
    # plt.legend()

fig, ax = plt.subplots()
part_a(sample_size, ax)
plt.legend()
plt.show()

# part b:
sample_sizes = [100, 150, 250]
fig, axis = plt.subplots(3, 1, figsize=(10, 15))
for i, sample_size in enumerate(sample_sizes):
    part_a(sample_size, axis[i])
    print('\n\n')
plt.legend()
plt.show()


# part c: Stratified Sampling - idk what ive done here (copilot ftw~)

# Define strata
strata_sizes = [180, 400, 250]  # Sizes of the strata
strata_means = [60, 65, 70]  # Means of the strata

# Generate samples from each stratum
strata_samples = []
for size, stratum_mean in zip(strata_sizes, strata_means):
    strata_samples.append(np.random.normal(stratum_mean, std_dev, size=size))

# Combine samples from different strata
stratified_sample = np.concatenate(strata_samples)

stratified_mean = np.mean(stratified_sample)
stratified_std_dev = np.std(stratified_sample)

plt.figure(figsize=(10, 5))
plt.hist(stratified_sample, bins=30, alpha=0.5, density=True, label='Stratified Sample')

x = np.linspace(20, 120, 1000)
plt.plot(x, norm_dist.pdf(x), 'k--', lw=2, label='Actual')

plt.legend()
plt.title('Histogram of Stratified Sample')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()

# Display statistics
print(f"Stratified Sample: \nMean = {stratified_mean:.3f}, \nStandard Deviation = {stratified_std_dev:.3f}")
