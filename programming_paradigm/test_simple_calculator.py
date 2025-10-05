# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Unit tests for the SimpleCalculator class, covering all arithmetic operations.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method is run.
        """
        self.calc = SimpleCalculator()

    # ------------------ Test Addition (add) ------------------

    def test_addition(self):
        """Test the addition method covering positive, negative, and float inputs."""
        # Positive integers
        self.assertEqual(self.calc.add(5, 3), 8)
        # Negative integers
        self.assertEqual(self.calc.add(-5, -3), -8)
        # Mixed integers
        self.assertEqual(self.calc.add(-10, 4), -6)
        # Floats
        self.assertEqual(self.calc.add(2.5, 1.5), 4.0)

    # ------------------ Test Subtraction (subtract) ------------------

    def test_subtraction(self):
        """Test the subtraction method covering positive, negative, and float inputs."""
        # Positive integers
        self.assertEqual(self.calc.subtract(10, 7), 3)
        # Negative result
        self.assertEqual(self.calc.subtract(5, 12), -7)
        # Subtraction involving negative numbers
        self.assertEqual(self.calc.subtract(5, -5), 10) 
        # Floats
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)

    # ------------------ Test Multiplication (multiply) ------------------

    def test_multiplication(self):
        """Test the multiplication method covering positive, negative, zero, and float inputs."""
        # Positive integers
        self.assertEqual(self.calc.multiply(6, 4), 24)
        # Multiplication by zero (edge case)
        self.assertEqual(self.calc.multiply(100, 0), 0)
        # Multiplication involving negative numbers
        self.assertEqual(self.calc.multiply(-5, 4), -20)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        # Floats
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    # ------------------ Test Division (divide) ------------------

    def test_division(self):
        """Test the division method covering normal operation, negative numbers, and division by zero."""
        # Normal division with integer result
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        # Division resulting in a float
        self.assertEqual(self.calc.divide(10, 4), 2.5)
        # Division involving negative numbers
        self.assertEqual(self.calc.divide(-10, 5), -2.0)
        # Critical edge case: division by zero
        # Asserts that the divide method correctly returns None when the denominator is 0
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))