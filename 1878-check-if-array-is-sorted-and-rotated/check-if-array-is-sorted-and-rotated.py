class Solution:
    def check(self, nums: List[int]) -> bool:
        if not nums:
            return True
        start = nums[0]
        flipped = False

        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1]:
                if flipped and nums[i] > start:
                    return False
                continue
            elif flipped or nums[i] > start:
                return False
            else:
                flipped = True
        return True