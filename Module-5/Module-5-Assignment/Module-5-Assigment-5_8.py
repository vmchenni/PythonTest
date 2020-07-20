# Draw a scatter graph of any 50 random values of x and y axis
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.show()