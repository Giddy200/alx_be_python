import math # Imported for completeness, though not strictly needed for the task

class Calculator:
    """
    A class demonstrating the use of static methods and class methods.
    """
    # Class Attribute: Accessible by class methods and static methods 
    # (though class methods access it via 'cls').
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method: Takes two arguments and returns their sum.
        It does not take 'self' or 'cls' and cannot access class or instance state.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method: Takes the class itself (cls) as its first argument.
        It uses 'cls' to access the class attribute calculation_type.
        """
        # Accessing the class attribute via the 'cls' parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()