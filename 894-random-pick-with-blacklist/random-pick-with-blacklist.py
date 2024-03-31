class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.b = sorted(blacklist)
        self.n = n

    def pick(self) -> int:
        k = random.randint(0, self.n - len(self.b) - 1) # exclusive
        left, right = 0, len(self.b) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if self.b[mid] - mid <= k:
                left = mid
            else:
                right = mid
        
        if left >= len(self.b):
            return k
        
        if self.b[right] - right <= k:
            return right + k + 1
        if self.b[left] - left <= k:
            return left + k + 1
        else:
            return k




# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()