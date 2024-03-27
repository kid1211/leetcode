class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.blacklist = sorted(blacklist)
        self.size = n

    def pick(self) -> int:
        k = random.randint(0, self.size - len(self.blacklist) - 1)
        left, right = 0, len(self.blacklist) - 1

        while left <= right:
            mid = (left + right) // 2 # +1?
            if self.blacklist[mid] - mid > k:
                right = mid - 1
            else:
                left = mid + 1
        
        return k + len(self.blacklist) if left >= len(self.blacklist) else k + left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()