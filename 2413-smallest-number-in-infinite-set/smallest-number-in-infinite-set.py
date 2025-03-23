class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.infiVal = 1
        self.lastPoppedHeapValue = 0
        # self.unique = set()

    def popSmallest(self) -> int:
        # if heap has value, and it is less than infit 
        # pop it, unless it is exactly the same as last time
        # 2 pop 4 pop 2 pop
        # 2 pop 1 pop 2 pop
        while self.heap:
            val = heappop(self.heap)
            if val == self.lastPoppedHeapValue:
                continue
            self.lastPoppedHeapValue = val
            return val
        # infi 5, add back 2
        self.infiVal += 1
        return self.infiVal - 1

    def addBack(self, num: int) -> None:
        # if heap has 2, and infi is only 1
        # i can pop 2, because i will see 2 any way
        # while self.heap and self.heap[0] >= self.infiVal:
        #     heappop(self.heap)
        if num >= self.infiVal:
            return
        self.lastPoppedHeapValue = min(self.lastPoppedHeapValue, num - 1)
        heappush(self.heap, num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)