class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        parity = nums[0] % 2

        for i in range(1, len(nums)):
            new = nums[i] % 2
            if parity == new:
                return False
            parity = new
        
        return True