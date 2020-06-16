import numpy as np

from lib import Variable


if __name__ == "__main__":
    x = Variable(np.array(2.0))
    y = x + np.array(3.0)
    print(f"result {y}, answer variable(5.0)")

    x = Variable(np.array(2.0))
    y = x + 3.0
    print(f"result {y}, answer variable(5.0)")

    x = Variable(np.array(2.0))
    y = 3.0 + x + 1.0
    print(f"result {y}, answer variable(6.0)")

    x = Variable(np.array(2.0))
    y = np.array([3.0]) + x
    print(f"result {y}, answer variable([5.0])")