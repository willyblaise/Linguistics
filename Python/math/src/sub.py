from src.ops import Operation


class Subtraction(Operation):
    def perform(self, operand1, operand2):
        return operand1 - operand2