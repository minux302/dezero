if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import numpy as np
from dezero import Variable


if __name__ == "__main__":
    x = Variable(np.array(1.0))
    y = (x + 3) ** 2
    y.backward()

    print(y)
    print(x.grad)

    x = Variable(np.array(2.0))
    y = - x
    print(f"result {y}, answer variable(-2.0)")

    x = Variable(np.array(2.0))
    y1 = 2.0 - x
    y2 = x - 1.0
    print(f"result {y1}, answer variable(0.0)")
    print(f"result {y2}, answer variable(1.0)")

    x = Variable(np.array(2.0))
    y1 = 1.0 / x
    y2 = x / 1.0
    print(f"result {y1}, answer variable(0.5)")
    print(f"result {y2}, answer variable(2.0)")

    x = Variable(np.array(2.0))
    y = x ** 3
    print(f"result {y}, answer variable(8.0)")
