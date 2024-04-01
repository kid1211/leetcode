class Solution:

    def __init__(self, w: List[int]):
        rolling = 0
        self.l = []
        for i in w:
            rolling += i
            self.l += [rolling]
        print(self.l)

    def pickIndex(self) -> int:
        target = random.randint(0, self.l[-1])
        left, right = 0, len(self.l) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if self.l[mid] <= target:
                left = mid
            else:
                right = mid

        return left if self.l[left] > target else right


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
[1, 3, 2]
[1, 4, 6] # 0 - 4 randomly pick, 0-> 0, 1, 5, -> 2