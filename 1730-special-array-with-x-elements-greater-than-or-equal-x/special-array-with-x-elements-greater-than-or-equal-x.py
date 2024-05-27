class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        lastMatched = -1
        for i in range(len(nums)):
            x = len(nums) - i
            # lastMatched = min(lastMatched, nu)
            # if nums[i] >= x:
            #     lastMatched = nums[i]

            # print(x, nums[i], nums[i] >= x, lastMatched >= x)
            if nums[i] >= x and not lastMatched >= x:
                return x
            lastMatched = nums[i]
        return -1


# 0 0 2 3 4
# 5 4 3 2 1

# 5 value greater than 5
# 4 values greater than 4
# 3 
# 2 values greater than 2