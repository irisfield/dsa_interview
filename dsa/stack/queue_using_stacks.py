class MyQueue:
    """
    232. Implement Queue using Stacks

    Intuition:
    Stacks are first-in-last-out (FILO), while queues are
    first-in-first-out (FIFO). In this implementation, `self.queue`
    maintains the order of elements in the queue, and `self.stack` is
    used to append elements to the back of the queue.
    """

    def __init__(self):
        self.queue = []
        self.stack = []

    def __queueify__(self):
        if len(self.queue) == 0:
            while self.stack:
                self.queue.append(self.stack.pop())

    def push(self, x: int) -> None:  # time O(1)
        self.stack.append(x)

    def pop(self) -> int:  # time amortized O(1)
        self.__queueify__()
        return self.queue.pop()

    def peek(self) -> int:  # time amortized O(1)
        self.__queueify__()
        return self.queue[-1]

    def empty(self) -> bool:  # time O(1)
        return len(self.queue) == 0 and len(self.stack) == 0
