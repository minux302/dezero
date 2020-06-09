import numpy as np

from lib import Variable, Add


if __name__ == "__main__":
    xs = [Variable(np.array(2)), Variable(np.array(3))]
    f = Add()
    ys = f(xs)
    print(ys[0].data)
    # x0, x1 = xs
    # print(x0 + x1)
    # sum_var = Variable(np.array(2)) + Variable(np.array(3))
    # print(sum_var)
