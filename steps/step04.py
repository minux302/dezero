import numpy as np

from lib import Variable, Square, Exp


def numerical_diff(f, x, eps=1e-4):
    y0 = f(Variable(x.data - eps))
    y1 = f(Variable(x.data + eps))
    return (y1.data - y0.data) / (2 * eps)


def f(x):
    A = Square()
    B = Exp()
    C = Square()
    return C(B(A(x)))


if __name__ == "__main__":
    # f = Square()
    # x = Variable(np.array(2.0))
    # dy = numerical_diff(f, x)
    # print(dy)
    x = Variable(np.array(0.5))
    dy = numerical_diff(f, x)
    print(dy)
