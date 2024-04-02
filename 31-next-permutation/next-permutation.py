class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 183265 -> 183526
        # 右边往左边升序结束的地方, 的前一位和最生序的开头swap,然后把后面reverse
        # 2, 5 swap
        # 183625

        # 87654321 => -1, 没得换, 直接reverse
        # 18765432 => 2, 1 swap 28765431, -> reversed 8765431

        # 3987421 => 4 和3换
        # 4987321 ==> reverse 4123789
        if len(nums) == 1:
            return

        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            for j in range(n - 1, -1, -1):
                if nums[j] > nums[i]:
                    break
            nums[i], nums[j] = nums[j], nums[i]
        print(nums)
        i, j = i + 1 if i >= 0 else 0, n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


        