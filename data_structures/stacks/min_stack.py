class MinStack:
    """155. Min Stack"""

    def __init__(self):
        self.stack = []
        self.min = []  # (idx, val)

    def push(self, val: int) -> None:
        idx = len(self.stack)
        if not self.stack:
            self.min.append((idx, val))
        elif val < self.min[-1][1]:
            self.min.append((idx, val))
        self.stack.append(val)

    def pop(self) -> None:
        if self.min and self.min[-1][0] == len(self.stack) - 1:
            self.min.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1][1] if self.min else 0

    # time O(1)
    # space O(n)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
