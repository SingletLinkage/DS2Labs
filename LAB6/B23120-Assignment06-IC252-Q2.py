from scipy.stats import norm, uniform, truncexpon
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# PART A

# Random Number Generators
# i. Uniform distribution
uniform_samples = uniform.rvs(size=10000)
ax.hist(uniform_samples, bins=10, density=True, alpha=0.5, label='Uniform', color='darkorange')

# ii. Normal distribution
normal_samples = norm.rvs(size=10000)
ax.hist(normal_samples, bins=30, density=True, alpha=0.5, label='Normal', color='green')

# iii. Truncated exponential distribution
truncexpon_samples = truncexpon.rvs(b=2, size=10000)
ax.hist(truncexpon_samples, bins=30, density=True, alpha=0.5, label='Truncated Exponential', color='tab:blue')

# Density Functions
# Uniform distribution
x = np.linspace(0, 1, 1000)
ax.plot(x, uniform.pdf(x), lw=2, label='Uniform', color='darkorange')

# Normal distribution
x = np.linspace(-4, 4, 1000)
ax.plot(x, norm.pdf(x), lw=2, label='Normal', color='green')

# Truncated exponential distribution
x = np.linspace(0, 6, 1000)
ax.plot(x, truncexpon.pdf(x, b=2), lw=2, label='Truncated Exponential', color='tab:blue')
ax.hlines(y=truncexpon.pdf(2, b=2), xmin=-4, xmax=2, color='tab:blue', lw=2, linestyle='--')
ax.hlines(y=truncexpon.pdf(0, b=2), xmin=-4, xmax=0, color='tab:blue', lw=2, linestyle='--')

# Just testing if anyone cares enough to remove this comment uwu
ax.set_title('Random Number Generators')
ax.set_xlabel('Value')
ax.set_ylabel('Density')
ax.set_xticks(np.arange(-4, 7, 1))
ax.hlines(y=1, xmin=-4, xmax=0, color='darkorange', lw=2, linestyle='--')
ax.legend()
plt.show()

# PART B

# pdf func:
# f(x) = (2x+3)/40 : 0<x<5 
# range of f(x) = 0.075 to 0.325

# cdf func:
# F(x) = (x^2 + 3x)/40 : 0<x<5

# for rv generation: calculation of inv-cdf
# x = (-3 + sqrt(9 + 160y))/2

# PDF func:
def pdf(x):
    if x < 0: return 0
    elif x > 5: return 0
    else: return (2*x+3)/40

# Inverse CDF func:
def inv_cdf(y):
    return (-3 + np.sqrt(9 + 160*y))/2

# Random Number Generator
random_samples = inv_cdf(np.random.uniform(0, 1, size=10000))

# Plotting
fig, ax = plt.subplots()
x = np.linspace(-2, 7, 1000)
ax.plot(x, [pdf(i) for i in x], color='tab:blue',  label='PDF')
ax.hist(random_samples, bins=20, density=True, alpha=0.5, label='Random Samples', color='tab:blue', edgecolor='tab:blue', lw=1)
ax.hlines(y=pdf(0), xmin=-2, xmax=0, color='tab:blue', lw=2, linestyle='--')
ax.hlines(y=pdf(5), xmin=-2, xmax=5, color='tab:blue', lw=2, linestyle='--')
ax.set_title('Random Number Generator')
ax.set_xlabel('Value')
ax.set_ylabel('Density')
ax.set_xticks(np.arange(-2, 8, 1))
ax.legend()
plt.show()