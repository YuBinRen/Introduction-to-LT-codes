import matplotlib.pyplot as plt
import numpy as np

N = 25
M = 13
d = 0.1
ls = []
for _ in range(N):
    if _ == 0:
        ls.append(0)
    elif _ < M-1:
        ls.append(1/(_*M))
    elif _ == M:
        ls.append(np.log(N/(M*d))/M)
    else:
        ls.append(0)

probabilities = [ 1 / N]
probabilities += [1 / (k * (k - 1)) for k in range(2, N+1)]

plt.bar(range(N),np.add(ls,probabilities))
plt.show()
