class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        def isContainOne():
            contain_one = False

            for i in range(n):
                if nums[i] == 1:
                    contain_one = True
                if nums[i] <= 0 or nums[i] > n:
                    nums[i] = 1
            return contain_one
        
        if not isContainOne():
            return 1
        
        for i in range(n):
            value = abs(nums[i])

            if value == n:
                nums[0] = - abs(nums[0])
            else:
                nums[value] = -abs(nums[value])
        
        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        return n if nums[0] > 0 else n + 1