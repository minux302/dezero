import numpy as np


class Variable:
    def __init__(self, data):
        self.data = data


class Function:
    def __call__(self, input):
        return Variable(self.forward(input.data))

    def forward(self, x):
        raise NotImplementedError()


class Square(Function):
    def forward(self, x):
        return x ** 2
