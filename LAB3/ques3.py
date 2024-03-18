from numpy.random import normal
import numpy as np
from statistics import NormalDist
from tabulate import tabulate

mean_weight = 150
std_dev_weight = 10

samples = 1000

distro = normal(mean_weight, std_dev_weight, samples)
temp = NormalDist(mean_weight, std_dev_weight)

headers = ['Event', 'Simulated', 'Theoretical']
data = []

# ----------- Part A ---------------
p_less_140 = np.where(distro < 140)[0].size / samples
data.append(['Probability that weight is less than 140 grams', p_less_140, round(temp.cdf(140), 2)])

# ----------- Part B ---------------
percentile_top5 = np.percentile(distro, 95)
top_5 = [i for i in distro if i > percentile_top5]
data.append(['Lowest weight for premium product (top 5%)', round(min(top_5), 2), round(temp.inv_cdf(0.95), 2)])

# ----------- Part C ---------------
percentile_lowest10 = np.percentile(distro, 10)
lowest_10 = [i for i in distro if i < percentile_lowest10]
data.append(['Highest Weight for defective product (lowest 10%)', round(max(lowest_10), 2), round(temp.inv_cdf(0.10), 2)])

# ----------- Part D ---------------
p_top_5 = len(top_5) / samples
p_lowest_10 = len(lowest_10) / samples
data.append(['Probability that product is neither premium nor defective', 
             1 - p_lowest_10-p_top_5, 
             1 - 0.10 - (1 - 0.95)])

print(tabulate(data, headers=headers, tablefmt='grid'))