class MinStack:
    """155. Min Stack"""

    def __init__(self):  # O(n) space
        self.stack = []
        self.min = []  # (idx, val)

    def push(self, val: int) -> None:  # O(1) time
        idx = len(self.stack)
        if not self.stack:
            self.min.append((idx, val))
        elif val < self.min[-1][1]:
            self.min.append((idx, val))
        self.stack.append(val)

    def pop(self) -> None:  # O(1) time
        if self.min and self.min[-1][0] == len(self.stack) - 1:
            self.min.pop()
        return self.stack.pop()

    def top(self) -> int:  # O(1) time
        return self.stack[-1]

    def getMin(self) -> int:  # O(1) time
        return self.min[-1][1] if self.min else 0
