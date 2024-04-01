class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.l = sorted(blacklist)
        self.n = n

    def pick(self) -> int:
        k = random.randint(0, self.n - len(self.l) - 1)
        if not self.l:
            return k
        left, right = 0, len(self.l) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2

            if self.l[mid] - mid <= k:
                left = mid
            else:
                right = mid

        if self.l[right] - right <= k:
            # print('right', right + k + 1)
            return right + k + 1
        elif self.l[left] - left <= k:
            # print('left', left + k + 1)
            return left + k + 1
        else:
            # print('less', k, left, right)
            return k

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()

# 2, 3, 5, 从7+3 (n - len(blacklist))里面挑选, 因为只有这么多个答案可以挑选
# k < 2, 就直接return k

# 2和3之间没有数值可以取

# 如果是 k = 2, 那我们应该顺位到4, 所以是k + 2, 这个2是要skip的black list的位置
# 所以我们是找, nums[mid] <= k + mid的最大值

# 超过了list的size 就是k + 总长度