from numpy.random import exponential
import matplotlib.pyplot as plt
import numpy as np

avg_cases_per_hr = 57
cases = 100000

distro = exponential(1/avg_cases_per_hr, cases)

# ----------------- Part A -----------------
# plt.plot(sorted(distro, reverse=True))
# plt.hist(distro, histtype='step', bins=100)
# freq, bins = np.histogram(distro, bins=1000)
# plt.plot(bins[:-1]*60, freq/cases)
# plt.show()
# lambda * e^(-lambda*x)

x = np.arange(0, 600)
y = 1/avg_cases_per_hr * np.exp(-1/avg_cases_per_hr * x)
plt.plot(x, y)
plt.show()

# ----------------- Part B -----------------
X = np.where(distro <= (1/60))[0]
print("Less than or equal to 1 min: ", len(X)/len(distro))

# ----------------- Part C -----------------
# X = np.where(distro < 2/60 and distro > 1/60)
X = np.where((distro < 2/60) & (distro > 1/60))[0]
print("Between 1 and 2 min: ", len(X)/len(distro))

# ----------------- Part D -----------------
X = np.where(distro > (2/60))[0]
print("Greater than 2 min: ", len(X)/cases)

# ----------------- Part E -----------------
print("After doubling of wait time: ")
avg_cases_per_hr *= 2
distro = exponential(1/avg_cases_per_hr, cases)
X = np.where((distro < 2/60) & (distro > 1/60))[0]
print("Between 1 and 2 min: ", len(X)/len(distro))
