# test_simple_calculator.py


import simple_calculator.py  as a SimpleCalculator
import unittest
from simple_calculator.py import SimpleCalculator

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
        self.assertEqual(self.calc.add(7, -7), 0)
        # Floats
        self.assertEqual(self.calc.add(2.5, 1.5), 4.0)

    # ------------------ Test Subtraction (subtract) ------------------

    # CONSOLIDATED TEST METHOD as requested
    def test_subtraction(self):
        """Test the subtraction method covering positive, negative, and float inputs."""
        # Positive integers
        self.assertEqual(self.calc.subtract(10, 7), 3)
        # Negative result
        self.assertEqual(self.calc.subtract(5, 12), -7)
        # Subtraction involving negative numbers (5 - (-5) = 10)
        self.assertEqual(self.calc.subtract(5, -5), 10) 
        # Subtraction with a negative result from negative numbers
        self.assertEqual(self.calc.subtract(-8, 2), -10)
        # Floats
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)

    # ------------------ Test Multiplication (multiply) ------------------

    def test_multiplication_positive_integers(self):
        """Test multiplication of two positive integers."""
        self.assertEqual(self.calc.multiply(6, 4), 24)

    def test_multiplication_by_zero(self):
        """Test multiplication where one factor is zero."""
        self.assertEqual(self.calc.multiply(100, 0), 0)
        
    def test_multiplication_mixed_integers(self):
        """Test multiplication involving negative numbers."""
        self.assertEqual(self.calc.multiply(-5, 4), -20)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiplication_floats(self):
        """Test multiplication with floating-point numbers."""
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    # ------------------ Test Division (divide) ------------------

    def test_division_normal(self):
        """Test normal division with an integer result."""
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        
    def test_division_float_result(self):
        """Test division resulting in a float."""
        self.assertEqual(self.calc.divide(10, 4), 2.5)

    def test_division_mixed_integers(self):
        """Test division involving negative numbers."""
        self.assertEqual(self.calc.divide(-10, 5), -2.0)

    def test_division_by_zero(self):
        """Test the edge case of division by zero."""
        # Asserts that the divide method returns None when the denominator is 0
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))