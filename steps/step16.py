import numpy as np

from lib import Function, Variable, square, add


if __name__ == "__main__":
    # generations = [2, 0, 1, 4, 2]
    # funcs = []

    # for g in generations:
    #     f = Function()
    #     f.generation = g
    #     funcs.append(f)

    # print([f.generation for f in funcs])
    x = Variable(np.array(2.0))
    a = square(x)
    y = add(square(a), square(a))
    y.backward()

    print(y.data)
    print(x.grad)
