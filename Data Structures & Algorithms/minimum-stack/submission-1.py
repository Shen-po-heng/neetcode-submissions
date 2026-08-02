class MinStack:

    def __init__(self):
        self.stack=list()
        self.min_stack = int()

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_stack = val
        elif val < self.min_stack:
            self.min_stack = val
        self.stack.append(val)

    def pop(self) -> None:
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
