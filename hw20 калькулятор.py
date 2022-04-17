class match:
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    def __init__(self, num_1, num_2, operation):
        self.num_1 = num_1
        self.num_2 = num_2
        self.operation = operation
    def calculate(self):
        operation = self.operations.get(self.operation)
        if operation:
            return operation(self.num_1, self.num_2)
answer = match(5, 10, '+').calculate()
print(answer)
