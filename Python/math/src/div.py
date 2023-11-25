from ops import Operation

class Division(Operation):
    def perform(self, operand1, operand2):
        if operand2 == 0:
            raise ValueError("Cannot divide by zero")
        return operand1 / operand2

    def perform(self, operand1, operand2):
        if operand2 == 0:
            raise ValueError("Cannot divide by zero")
        return operand1 / operand2