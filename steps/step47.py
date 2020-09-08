if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
from dezero import Variable, Model
import dezero.functions as F
from dezero.models import MLP
from dezero import optimizers


if __name__ == "__main__":
    # x = Variable(np.array([[1, 2, 3], [4, 5, 6]]))
    # print(x[1])
    # print(x[:, 2])
    x = np.array([[0.2, -0.4], [0.3, 0.5], [1.3, -3.2], [2.1, 0.3]])
    t = np.array([2, 0, 1, 0])
    model = MLP((10, 3))
    y = model(x)
    loss = F.softmax_cross_entropy_simple(y, t)
    print(loss)