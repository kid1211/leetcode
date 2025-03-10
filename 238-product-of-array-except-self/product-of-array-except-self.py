class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # forward and backward,
        res = []
        rolling = 1

        for num in nums:
            res += [rolling]
            rolling *= num
        # print(res)

        rolling = 1
        for i in range(len(res) - 1, -1, -1):
            res[i] *= rolling
            rolling *= nums[i]
        
        return res

        