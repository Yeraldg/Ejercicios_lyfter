import unittest
from unittest.mock import mock_open, patch 
#ejercicio 1

def sum(a, b):
    return a + b
    
def average(a, b):
    return (a +b) / 2
    
def multiply (a, b):
    return a * b

class Test_numbers(unittest.TestCase):
    def test_sum_positive(self):
        self.assertEqual(sum(5, 3), 8)
    def test_sum_negative(self):
        self.assertEqual(sum(-5, -3), -8)
    def test_sum_zero(self):
        self.assertEqual(sum(0, 0), 0)
        
    #ejercicio 2
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)
    def test_divide_zero(self):
        with self.assertRaises(ValueError):
            divide (10, 0)
    def test_divide_string(self):
        with self.assertRaises(TypeError):
            divide("10", 2)
    
    #ejercicio 3
    def test_read_lines(self):
        content = "Hello\nPython\nUnit Testing\n"
        mock_file = mock_open(read_data=content)
        with patch("builtins.open", mock_file):
            result = read_lines("fake_file.txt")
        self.assertEqual(
            result,
            ["Hello\n", "Python\n", "Unit Testing\n"])
    
    def test_read_lines_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                read_lines("nonexisting_file.txt")

#ejercicio 2

def divide(number1, number2):
    if number2 == 0:
        raise ValueError("unable to divide by 0")
    return number1 / number2

#ejercicio 3

def read_lines(path):
    with open(path, 'r') as f:
        return f.readlines()


if __name__ == "__main__":
    unittest.main()

