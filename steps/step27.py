if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import math

import numpy as np
from dezero import Variable
from dezero.core_simple import sin
from dezero.utils import plot_dot_graph


def my_sin(x, threshold=1e-150):
    y = 0
    for i in range(100000):
        c = (-1) ** i / math.factorial(2 * i + 1)
        t = c * x ** (2 * i + 1)
        y = y + t
        if abs(t.data) < threshold:
            break
    return y


if __name__ == "__main__":
    x = Variable(np.array(np.pi/4))
    # y = sin(x)
    y = my_sin(x)
    y.backward()

    print(y.data)
    print(x.data)
    plot_dot_graph(y, verbose=False, to_file='sample.png')
