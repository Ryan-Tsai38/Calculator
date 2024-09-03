import matplotlib.pyplot as plt
import numpy as np

class Grapher:
    def __init__(self):
        pass

    def plot_function(self, func, x_range):
        x = np.linspace(x_range[0], x_range[1], 400)
        y = eval(func)
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Graph of {func}')
        plt.grid(True)
        plt.show()