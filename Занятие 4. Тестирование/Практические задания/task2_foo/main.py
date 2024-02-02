import unittest
from add import Calculator


class TestStringMethods(unittest.TestCase):
    print("TestString")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)



class TestCalculator(unittest.TestCase):
    print("TestCalculator")

    def test_add(self):
        print("test_add")
        self.assertEqual(Calculator.add(5, 3), 8)

    def test_color(self):
        self.assertEqual(calc.set_color('white'), calc.color)



if __name__ == '__main__':
    unittest.main()
    calc = Calculator(5)
    calc.set_color('red')
    print(calc.color)