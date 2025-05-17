class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counting sort
        count = Counter(nums)

        k = 0
        for i in range(3):
            for j in range(count[i]):
                nums[k] = i
                k += 1
