class MinStack:

    def __init__(self):
        self.min_stacks = []
        self.minimum = []

    def push(self, value: int) -> None:
        self.min_stacks.append(value)

        if not self.minimum or value <= self.minimum[-1]:   
            self.minimum.append(value)

    def pop(self) -> None:
        value = self.min_stacks.pop()

        if value == self.minimum[-1]:   
            self.minimum.pop()

    def top(self) -> int:
        return self.min_stacks[-1]

    def getMin(self) -> int:
        return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()