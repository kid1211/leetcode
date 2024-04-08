from sortedcontainers import SortedList
class MaxStack:

    def __init__(self):
        self.idx = 0
        self.normal = SortedList()
        self.maxValues = SortedList()

    def push(self, x: int) -> None:
        idx = self.idx
        self.normal += [(idx, x)]
        self.maxValues += [(x, idx)]
        self.idx += 1

    def pop(self) -> int:
        idx, val = self.normal.pop()
        self.maxValues.remove((val, idx))
        return val

    def top(self) -> int:
        return self.normal[-1][1] if self.normal else -1

    def peekMax(self) -> int:
        return self.maxValues[-1][0] if self.normal else -1
        

    def popMax(self) -> int:
        val, idx = self.maxValues.pop()
        self.normal.remove((idx, val))
        return val
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()