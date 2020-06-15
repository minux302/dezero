import time
import numpy as np

from lib import Variable, square


if __name__ == "__main__":
    start = time.time()
    for i in range(100000):
        x = Variable(np.random.randn(1000))
        y = square(square(square(x)))
    print(time.time() - start)
