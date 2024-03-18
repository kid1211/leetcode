class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        rolling = 0

        # k >= 3
        for i in range(2):
            rolling += nums[i]

        res = None
        for i in range(2, len(nums)):
            target = nums[i]

            if rolling > target:
                res = target + rolling

            rolling += target

        return res if res is not None else -1
    

# k >= 3

# [1,12,1,2,5,50,3] sorted =>
# [1, 1, 2, 3, 5, 12, 50]
# [1  2  4. 7, 12, 24, 74]

# greedy 不存在少增加 反而更大
