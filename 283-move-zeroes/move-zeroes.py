class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return

        j = 0
        for i in range(n):
            if nums[i] != 0:
                continue
            j = max(j, i + 1)
            while j < n and nums[j] == 0:
                j += 1
            # print(j)
            if j < n:
                nums[i], nums[j] = nums[j], nums[i]


        # j = 0
        # for i in range(n):
        #     if nums[i] != 0:
        #         continue

        #     j = i
        #     while j < n and nums[j] != '0':
        #         j += 1
# 1 , 2, 3, 4, 0, 0 , 0, 8
# j == i == 0
#     i