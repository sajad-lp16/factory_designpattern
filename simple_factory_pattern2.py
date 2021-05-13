from abc import ABCMeta, abstractmethod


class AbstractOperations(metaclass=ABCMeta):

    def __init__(self, operand_a, operand_b):
        self.operand_a = operand_a
        self.operand_b = operand_b
        super().__init__()

    @abstractmethod
    def execute(self):
        pass


class AddOperation(AbstractOperations):
    def execute(self):
        return self.operand_a + self.operand_b


class Multiply(AbstractOperations):
    def execute(self):
        return self.operand_a * self.operand_b


class Division(AbstractOperations):
    def execute(self):
        return self.operand_a // self.operand_b


class Subtraction(AbstractOperations):
    def execute(self):
        return self.operand_a - self.operand_b
