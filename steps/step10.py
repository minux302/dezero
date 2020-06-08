import unittest

import numpy as np

from lib import square, Variable, numerical_diff


class SquareTest(unittest.TestCase):
    def test_forward(self):
        x = Variable(np.array(2.0))
        self.assertEqual(square(x).data, np.array(4.0))

    def test_backward(self):
        x = Variable(np.array(3.0))
        y = square(x)
        y.backward()
        self.assertEqual(x.grad, np.array(6.0))

    def test_gradient_check(self):
        x = Variable(np.array(0.5))
        y = square(x)
        y.backward()
        self.assertTrue(
            np.allclose(x.grad, numerical_diff(square, x))
        )


if __name__ == "__main__":
    unittest.main()
