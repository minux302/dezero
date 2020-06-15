import numpy as np

from lib import Variable


if __name__ == "__main__":
    x = Variable(np.array([[1, 2, 3], [4, 5, 6]]))
    print("shape: ", x.shape)
    print("dim: ", x.ndim)
    print("size: ", x.size)
    print("dtype: ", x.dtype)
    print("len: ", len(x))
    print(x)

    x = Variable(None)
    print(x)
    x = Variable(np.array([1, 2, 3]))
    print(x)
