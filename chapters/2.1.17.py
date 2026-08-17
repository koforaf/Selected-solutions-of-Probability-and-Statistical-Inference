import numpy as np
import matplotlib.pyplot as plt
from math import comb

# Possible values of X
x = np.arange(0, 6)

# Hypergeometric probability mass function
prob = np.array([
    comb(12, k) * comb(40, 5-k) / comb(52, 5)
    for k in x
])

print(prob)

# Plot probability histogram
plt.bar(x, prob)

plt.xlabel("Number of face cards, X")
plt.ylabel("Probability P(X = x)")
plt.title("Probability Histogram of X")
plt.xticks(x)

plt.show()

###############################

x = np.arange(0, 6)

# Theoretical probability
prob = np.array([
    comb(12, k) * comb(40, 5-k) / comb(52, 5)
    for k in x
])

# Observed data
data = np.array([
    2, 1, 2, 1, 0, 0, 1, 0, 1, 1,
    0, 2, 0, 2, 3, 0, 1, 1, 0, 3,
    1, 2, 0, 2, 0, 2, 0, 1, 0, 1,
    1, 2, 1, 0, 1, 1, 2, 1, 1, 0
])

counts = np.bincount(data, minlength=6)
relative_freq = counts / len(data)

# Width of each bar
width = 0.35

plt.bar(
    x - width/2,
    prob,
    width=width,
    label="Theoretical Probability"
)

plt.bar(
    x + width/2,
    relative_freq,
    width=width,
    label="Observed Relative Frequency"
)

plt.xlabel("Number of face cards, X")
plt.ylabel("Probability / Relative Frequency")
plt.title("Theoretical Distribution vs. Observed Data")

plt.xticks(x)
plt.legend()
plt.show()