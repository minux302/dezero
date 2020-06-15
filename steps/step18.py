import numpy as np

from lib import Variable, add, no_grad


if __name__ == "__main__":
    with no_grad():
        x0 = Variable(np.array(1.0))
        x1 = Variable(np.array(1.0))
        t = add(x0, x1)
        y = add(x0, t)
        # y.backward()