# Using the 'typing' module for more complex types
from typing import List, Tuple

def add_numbers(a: int, b: int) -> int:
    return a + b


def calculate_stats(data: List[float]) -> Tuple[float, float, float]:
    total = sum(data)
    average = total / len(data)
    maximum = max(data)
    return total, average, maximum

result = add_numbers(5, 3)
print(result)  # Outputs: 8

data = [10.2, 15.5, 8.7, 12.1]
total, average, maximum = calculate_stats(data)
print(f"Total: {total}, Average: {average}, Maximum: {maximum}")
