from abc import ABC, abstractmethod


class Operation(ABC):
    @abstractmethod
    def perform(self, operand1, operand2):
        pass