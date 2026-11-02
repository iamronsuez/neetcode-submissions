class MinStack:

    def __init__(self):
        self.stack = []
        self.minimumStack = []
    def push(self, val: int) -> None:
        if self.minimumStack:
            self.minimumStack.append(min(val, self.minimumStack[-1]))
        else:
            self.minimumStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimumStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimumStack[-1]