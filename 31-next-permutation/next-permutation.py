class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        1. find pivot, from right to left increasing
        2. swap pivot find the largest number that is larger than the pivot
        3. reverse the res

        1 8 3 2 6 5
        """
        n = len(nums)

        if n == 1:
            return
        # 1
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2
        if i != -1:
            for j in range(n - 1, -1, -1):
                if nums[j] > nums[i]:
                    break
            nums[i], nums[j] = nums[j], nums[i]

        # 3
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

        # if i >= 0:


"""
1, 2, 3, 4, 5
2, 1, 3, 4, 5


1, 2, 5, 3, 4
1, 2, 5, 4, 3
1, 5, 2, 3, 4
1, 5, 2, 4, 3
"""
        