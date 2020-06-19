if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import numpy as np
from dezero import Variable
from step24 import goldstein
from dezero.utils import _dot_func, _dot_var, plot_dot_graph


if __name__ == "__main__":
    # x0 = Variable(np.array(1.0))
    # x1 = Variable(np.array(1.0))
    # y = x0 + x1
    # y.backward()
    # x0.name = 'x0'
    # x1.name = 'x1'
    # y.name = 'y'
    # plot_dot_graph(y, verbose=False, to_file='sample.png')

    x = Variable(np.array(1.0))
    y = Variable(np.array(1.0))
    z = goldstein(x, y)
    z.backward()

    x.name = 'x'
    y.name = 'y'
    x.name = 'z'
    plot_dot_graph(z, verbose=False, to_file='sample.png')