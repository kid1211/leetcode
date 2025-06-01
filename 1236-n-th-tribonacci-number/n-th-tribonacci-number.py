class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        # if n == 3:
        #     return 0 + 1 + 1
        # if n == 3:
        #     return 1 + 2 + 3
        return  self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)