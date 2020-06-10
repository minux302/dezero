import numpy as np
from lib import Variable, add


if __name__ == "__main__":
    x = Variable(np.array(3.0))
    # y = add(x, x)
    # y.backward()
    # print(x.grad)

    # x.cleargrad()
    # y = add(add(x, x), x)
    z = add(x, x)
    y = add(z, x)
    y.backward()
    print(x.grad)
