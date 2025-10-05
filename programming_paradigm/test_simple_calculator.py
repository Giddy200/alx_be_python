# test_simple_calculator.py

import simple_calculator.py as simple_calculator
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

    def test_addition_positive_integers(self):
        """Test addition with two positive integers."""
        self.assertEqual(self.calc.add(5, 3), 8)
    
    def test_addition_negative_integers(self):
        """Test addition with two negative integers."""
        self.assertEqual(self.calc.add(-5, -3), -8)
    
    def test_addition_mixed_integers(self):
        """Test addition with a positive and a negative integer."""
        self.assertEqual(self.calc.add(-10, 4), -6)
        self.assertEqual(self.calc.add(7, -7), 0)
        
    def test_addition_floats(self):
        """Test addition with floating-point numbers."""
        self.assertEqual(self.calc.add(2.5, 1.5), 4.0)
        self.assertEqual(self.calc.add(0.1, 0.2), 0.30000000000000004) # standard float behavior
        # Use assertAlmostEqual for better float comparison in general, but assertEqual is acceptable here.

    # ------------------ Test Subtraction (subtract) ------------------

    def test_subtraction_positive_integers(self):
        """Test subtraction with positive integers."""
        self.assertEqual(self.calc.subtract(10, 7), 3)

    def test_subtraction_negative_result(self):
        """Test subtraction resulting in a negative number."""
        self.assertEqual(self.calc.subtract(5, 12), -7)
        
    def test_subtraction_mixed_integers(self):
        """Test subtraction involving negative numbers."""
        self.assertEqual(self.calc.subtract(5, -5), 10) # 5 - (-5) = 10
        self.assertEqual(self.calc.subtract(-8, 2), -10)
        
    def test_subtraction_floats(self):
        """Test subtraction with floating-point numbers."""
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

    def test_division_by_one(self):
        """Test division by 1."""
        self.assertEqual(self.calc.divide(99, 1), 99.0)

    def test_division_mixed_integers(self):
        """Test division involving negative numbers."""
        self.assertEqual(self.calc.divide(-10, 5), -2.0)
        self.assertEqual(self.calc.divide(10, -5), -2.0)
        self.assertEqual(self.calc.divide(-10, -5), 2.0)

    def test_division_by_zero(self):
        """Test the edge case of division by zero."""
        # The class documentation says it returns None for division by zero
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))


# The tests can be run using: python -m unittest test_simple_calculator.py