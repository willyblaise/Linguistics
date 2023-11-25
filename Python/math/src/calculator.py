from src.ops import Operation

class Calculator:
    @staticmethod
    def calculate(operation, operand1, operand2):
        if isinstance(operation, Operation):
            return operation.perform(operand1, operand2)
        else:
            raise ValueError("Invalid operation provided to the calculator")