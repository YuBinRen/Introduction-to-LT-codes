
import matplotlib.pyplot as plt
import numpy as np

N = 25
probabilities = [ 1 / N]
probabilities += [1 / (k * (k - 1)) for k in range(2, N+1)]
probabilities_sum = sum(probabilities)

plt.bar(range(N),probabilities)
plt.show()