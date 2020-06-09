import numpy as np

from lib import Variable, Add, add


if __name__ == "__main__":
    x0 = Variable(np.array(2))
    x1 = Variable(np.array(3))
    # f = Add()
    # y = f(x0, x1)
    y = add(x0, x1)
    print(y.data)
