class StockSpanner:

    def __init__(self):
        self.stack = []


    def next(self, price: int) -> int:
        res = 1

        while self.stack and self.stack[-1][0] <= price:
            _, last = self.stack.pop()
            res += last
        self.stack += [(price, res)]
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)