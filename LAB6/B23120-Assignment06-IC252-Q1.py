import numpy as np
import matplotlib.pyplot as plt
from statistics import NormalDist

# PART A
# entropy of fair coin calculation:
p = [0.5, 0.5]

H = -np.sum(p*np.log2(p))
print(f'Entropy of Fair Coin: {H:.4f}')

# biased coin with X-axis : p(head)
p_head = np.linspace(0, 1, 1000)[1:-1]
H = np.zeros_like(p_head)

for i, p in enumerate(p_head):
    H[i] = -np.sum([p, 1-p]*np.log2([p, 1-p]))

fig, ax = plt.subplots()
ax.plot(p_head, H)
ax.vlines(x=0.5, ymin=0, ymax=1, color='red', linestyle='--')
ax.hlines(y=1, xmin=0, xmax=0.5, color='red', linestyle='--')
ax.plot(0.5, 1, 'ro')
ax.annotate('(0.5, 1)', (0.5, 1.01))
ax.set_xlabel('p(head)')
ax.set_ylabel('Entropy')
ax.set_title('Entropy vs Probability of Head')
plt.show()

# PART B
def plot(mu_a, mu_b, sigma_a, sigma_b, ax, type):
    A = NormalDist(mu_a, sigma_a)
    B = NormalDist(mu_b, sigma_b)

    x = np.linspace(-10, 10, 1000)
    # Generating PDF values for A and B
    y_a = np.array([A.pdf(i) for i in x])
    y_b = np.array([B.pdf(i) for i in x])

    # Normalization
    y_a /= np.sum(y_a)
    y_b /= np.sum(y_b)

    # Calculation of KL Divergence and Cross Entropy
    KL = sum(y_a * np.log2(y_a/y_b))
    CE = sum(-y_a * np.log2(y_b))

    # ====================================================
    #                          ISSUE
    # Value of CE getting influenced by the number of pts in x
    # Normalization reduced the incluence (and actually make KL almost independent)
    # but still CE is not completely independent whyyyyyyyyyyyyyyyyyyyyyyyyyyy sed life
    # ====================================================

    ax.plot(x, y_a, label='A', color='red', alpha=0.5)
    ax.plot(x, y_b, label='B', color='tab:blue')
    ax.fill_between(x, y_a, color='lightcoral', alpha=0.5)
    ax.fill_between(x, y_b, color='lightblue', alpha=0.5)
    ax.vlines(x=mu_a, ymin=0, ymax=max(y_a), color='red', linestyle='--')
    ax.vlines(x=mu_b, ymin=0, ymax=max(y_b), color='tab:blue', linestyle='--')
    ax.set_ylabel('PDF')
    ax.set_title(f'Normal Distributions : {type}')
    ax.set_xticks(np.arange(-10, 11, 1))
    ax.text(0.1, 0.5, f'KL Divergence: {KL:.4f}\nCross Entropy: {CE:.4f}', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
    ax.text(0.9, 0.5, f'{mu_a=}\n{mu_b=}\n{sigma_a=}\n{sigma_b=}', horizontalalignment='left', verticalalignment='center', transform=ax.transAxes)

    ax.legend()


fig, ax = plt.subplots(3, 1, figsize=(15, 12))
# Part i
plot(1, 1, 1, 1, ax[0], 'Overlap')
# Part ii
plot(0, 2, 1, 1, ax[1], 'Partially Overlap')
# Part iii
plot(-5, 5, 1, 1, ax[2], 'Do Not Overlap')
ax[2].set_xlabel('X')
plt.show()