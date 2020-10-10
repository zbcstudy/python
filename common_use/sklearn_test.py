from sklearn import datasets
import matplotlib.pyplot as plt

x, y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=1)
plt.figure()
plt.scatter(x, y)
plt.show()
