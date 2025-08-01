class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        n = len(nums)
        l = 1
        for r in range(1, n):
            if nums[r] == nums[l - 1]:
                continue
            nums[l] = nums[r]
            l += 1
            # if l == 0 or nums[l]
        return l

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         n = len(nums)

#         j = 0
#         last_update = 0
#         for i in range(n):
#             while j < n and nums[i - 1] == nums[j]:
#                 j += 1
#             if j < n:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 j += 1
#                 last_update = max(last_update, i)
#         return last_update + 1