class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElement = max(nums)
        maxCount = 0
        

        left = res = 0
        for right in range(len(nums)):
            if nums[right] == maxElement:
                maxCount += 1

            while left <= right and maxCount == k:
                if nums[left] == maxElement:
                    maxCount -= 1
                left += 1
            res += left
        return res

# 0 1 2  3 4  5 6 7 8  9 10 11 12 13 14
# 4 3 7 10 2 10 1 6 10 7 10 10  9  8  3, k = 3, max=10
# LS    LE          R
# From LS-LE for starting point are all valid
# so res += 4

# 0 1 2  3 4  5 6 7 8  9 10 11 12 13 14
# 4 3 7 10 2 10 1 6 10 7 10 10  9  8  3, k = 3, max=10
#        L           R
# res += 2 * 2