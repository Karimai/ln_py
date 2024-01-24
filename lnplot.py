import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(-5, 5, 100)
# y = 0.5 * x + 1

x = np.linspace(-5, 5, 10000000)
y = np.tan(x)

plt.axhline(y=0, color='blue')  # to draw a horizontal line across the axes.
plt.axvline(x=0, color='red')  # to draw a horizontal line across the axes.
plt.grid()
plt.plot(x, y, label='x ** 2')
plt.legend()
plt.show()

