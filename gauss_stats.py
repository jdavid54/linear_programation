import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(13)
x = np.linspace(-2, 6, 500)
pi = stats.dirichlet([1, 1, 1]).rvs()[0]
mu = stats.norm(1, 1).rvs(3)

y = stats.norm(mu, np.ones(3)).pdf(x[:, None])
plt.figure(figsize=(12, 6))
plt.title('Gaussian Mixture model')
plt.ylabel(r'$P(x)$')
plt.xlabel(r'$X$')

plt.plot(x, y[:, 1] * pi[1], ls='--')
plt.plot(x, y[:, 2] * pi[2], ls='--')
plt.plot(x, y[:, 0] * pi[0], ls='--')

for i in range(3):
    xi = x[np.argmax(y[:, i])]
    yi = (y[:, i] * pi[i]).max()
    plt.vlines(xi, 0, yi)
    plt.text(xi + 0.05, yi + 0.01, r'$\pi_{}$'.format(i + 1))
plt.plot(x, (y * pi).sum(1))
plt.show()
