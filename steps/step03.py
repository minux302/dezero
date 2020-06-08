import numpy as np

from lib import Function, Variable, Square


class Exp(Function):
    def forward(self, x):
        return np.exp(x)


if __name__ == "__main__":
    A = Square()
    B = Exp()
    C = Square()

    x = Variable(np.array(0.5))
    a = A(x)
    b = B(a)
    c = C(b)
    print(c.data)
