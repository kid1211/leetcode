from sortedcontainers import SortedList

class MaxStack:

    def __init__(self):
        self.stack = SortedList()
        self.value = SortedList()
        self.cnt = 0

    def push(self, x: int) -> None:
        self.stack += [(self.cnt, x)]
        self.value += [(x, self.cnt)]
        self.cnt += 1

    def pop(self) -> int:
        stackItem = self.stack.pop()
        self.value.remove(stackItem[::-1])
        return stackItem[1]

    def top(self) -> int:
        return self.stack[-1][1]

    def peekMax(self) -> int:
        return self.value[-1][0]
        
    def popMax(self) -> int:
        valueItem = self.value.pop()
        self.stack.remove(valueItem[::-1])
        return valueItem[0]


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()