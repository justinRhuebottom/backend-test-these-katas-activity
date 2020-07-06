import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        """Test if katas.add() correctly returns added value"""
        self.assertEqual(katas.add(3, 3), 6)

    def test_multiply(self):
        """Test if katas.multiply() correctly returns multiplied value"""
        self.assertEqual(katas.multiply(3, 3), 9)

    def test_power(self):
        """Test if katas.power() correctly returns x to the power of n"""
        self.assertEqual(katas.power(3, 3), 27)

    def test_factorial(self):
        """Test if katas.factorial() correctly returns factorial value"""
        self.assertEqual(katas.factorial(3), 6)

    def test_fibonacci(self):
        """Test if katas.fibonacci() correctly returns value of n location in fobonacci sequence"""
        self.assertEqual(katas.fibonacci(3), 1)


if __name__ == '__main__':
    unittest.main()
