import unittest  

from calculator import add, multiply, sqrt, squared, fibonacci


# test for calculator functionalities
class Calculator(unittest.TestCase):
    def testSum(self):
        self.assertEqual(6, reduce(add, [1, 2, 3]))

    def testFilterOdd(self):
        self.assertEqual([1, 3], filter(lambda x: x % 2 == 1, [1, 2, 3, 4]))

    def testFilterEven(self):
        self.assertEqual([2, 4], filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))

    def testMultiplication(self):
        self.assertEqual(6, reduce(multiply, [1, 2, 3]))

    def testSquare(self):
        self.assertEqual([4, 9, 16], map(squared, [2, 3, 4]))

    def testSquareRoot(self):
        self.assertEqual([2, 3, 4], map(sqrt, [4, 9, 16]))

    def testPower(self):
        self.assertEqual([2, 4, 8], [2 ** x for x in range(1, 4)])

    def testFibonacci(self):
        self.assertEqual([0, 1, 1, 2, 3, 5], [x for x in fibonacci(5)])


if __name__ == "__main__":
    unittest.main()
