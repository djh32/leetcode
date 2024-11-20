import numpy as np  
import matplotlib.pyplot as plt 
from scipy import stats

X = np.linspace(0, 1600, 10)

std = 0.693147182
mean = 1
lognorm_distribution = stats.lognorm([std], loc=mean)
lognorm_distribution_pdf = lognorm_distribution.pdf(X)
fig, ax = plt.subplots(figsize=(8, 5))
plt.plot(X, lognorm_distribution_pdf, label="μ=0, σ=1")
ax.set_xticks(X)
plt.show()