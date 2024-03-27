class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.blacklist = sorted(blacklist)
        self.size = n

    def pick(self) -> int:
        k = random.randint(0, self.size - len(self.blacklist) - 1)
        left, right = 0, len(self.blacklist) - 1

        while left + 1 < right:
            mid = (left + right) // 2 # +1?
            #find the largest blacklist[mid] less than the W[k]
            if self.blacklist[mid] - mid > k:
                right = mid
            else:
                left = mid
        
        print(left, right, len(self.blacklist))
        print('2', k, k + left, + 1, k + right + 1)

        if left >= len(self.blacklist):
            return k

        if self.blacklist[right] - right <= k:
            return k + right + 1
        elif self.blacklist[left] - left <= k:
            return k + left + 1
        return k

# 0   1. 2. 3. 4. 5.  6. 7.    8
# [2, 4, 6, 7, 9, 10, 11, 13, 17]
# [2, 3, 4, 4, 5,  5,  5,  6,  9] 

# k == 0, 0
# k == 1, 1
# k == 2, 2 + 1 + 0. <= 2
# k == 3, 3 + 1 + 1 == 5
# k == 4, 4 + 1 + 3 == 8
# k == 5, 5 + 1 + 6 == 12
# k == 6, 6 + 1 + 7 == 14
# k == 7, 7 + 1 + 7 == 15
# k == 8, 8 + 1 + 7 == 16
# k == 9, 9 + 1 + 8 == 18
# return lo == hi && b[lo] - lo <= k ? k + lo + 1 : k;
        
# total - blacklist = whitelist range


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()