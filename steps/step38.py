if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import numpy as np
from dezero import Variable
import dezero.functions as F


if __name__ == "__main__":
    x = Variable(np.array(
        [[1, 2, 3], [4, 5, 6]]
    ))
    y = F.reshape(x, (6,))
    y.backward(retain_grad=True)
    print(x.grad)

    x = Variable(np.random.rand(2, 3))
    # y = x.transpose()
    y = x.T
    print(y.shape)