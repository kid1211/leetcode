class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def twosum(target, startIdx):
            left, right = startIdx, n - 1
            res = []
            while left < right:
                tmp = target + nums[left] + nums[right]
                if tmp == 0:
                    res += [[target, nums[left], nums[right]]]

                    # skip the same values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                if tmp > 0:
                    right -= 1
                else:
                    left += 1
            return res

        res = []
        nums.sort() # 去重1/3, 如果两个数相同就只取第一个
        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue # 去重2/3
            res += twosum(nums[i], i + 1)
        return res
