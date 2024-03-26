class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        def hasOne():
            hasOne = False
            for i in range(n):
                if nums[i] == 1:
                    hasOne = True
                elif nums[i] > n or nums[i] <= 0:
                    nums[i] = 1

            return hasOne
        
        if not hasOne():
            return 1
        
        for i in range(n):
            val = abs(nums[i])
            # 1 is present, nums[i] == 1, we want nums[1] be negative
            # -2 is present, nums[i] == abs(-2), we want to makr nums[2]
            if val == n:
                nums[0] = - abs(nums[0])
            else:
                nums[val] = -abs(nums[val])

        for i in range(1, n):
            if nums[i] > 0:
                return i
        return n if nums[0] > 0 else n + 1