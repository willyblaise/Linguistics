from abc import ABC, abstractmethod
from src.add import Addition
from src.ops import Operation
from src.sub import Subtraction
from src.mult import Multiplication
from src.div import Division
from src.calculator import Calculator


# Example usage:

# Create instances of operations
addition = Addition()
subtraction = Subtraction()
multiplication = Multiplication()
division = Division()

# Use the Calculator to perform operations
result_add = Calculator.calculate(addition, 5, 3)
result_sub = Calculator.calculate(subtraction, 8, 2)
result_mul = Calculator.calculate(multiplication, 4, 6)
result_div = Calculator.calculate(division, 9, 3)

# Display the results
print(f"Addition Result: {result_add}")
print(f"Subtraction Result: {result_sub}")
print(f"Multiplication Result: {result_mul}")
print(f"Division Result: {result_div}")