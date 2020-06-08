import numpy as np

from lib import Variable, square, exp


if __name__ == "__main__":
    x = Variable(np.array(0.5))
    a = square(x)
    b = exp(a)
    y = square(b)

    # y.grad = np.array(1.0)
    y.backward()
    print(x.grad)

    # x = Variable(None)
    # x = Variable(1.0)
