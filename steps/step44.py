if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
from dezero import Variable
import dezero.functions as F
import dezero.layers as L


if __name__ == "__main__":
    np.random.seed(0)
    x = np.random.rand(100, 1)
    y = np.sin(2 * np.pi * x) + np.random.rand(100, 1)

    l1 = L.Linear(10)
    l2 = L.Linear(1)

    lr = 0.2
    iters = 1000

    def predict(x):
        y = l1(x)
        y = F.sigmoid(y)
        y = l2(y)
        return y

    for i in range(iters):
        y_pred = predict(x)
        loss = F.mean_squared_error(y, y_pred)
        loss.backward()

        for l in [l1, l2]:
            for p in l.params():
                p.data -= lr * p.grad.data
        if i % 1000 == 0:
            print(loss)

