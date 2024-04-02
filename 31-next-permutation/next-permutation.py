class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # 183265 -> 183526
        # 右边往左边升序结束的地方, 的前一位和醉生序的开头swap,然后把后面reverse
        # 2, 5 swap
        # 183625

        # 87654321 => -1, 没得换, 直接reverse
        # 18765432 => 2, 1 swap 28765431, -> reversed 8765431

        # 3987421 => 4 和3换
        # 4987321 ==> reverse
            # 4123789
        if len(nums) == 1:
            return

        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break

        for j in range(n - 1, -1, -1):
            if nums[j] > nums[i]:
                break
        print(i, j)
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

        i, j = i + 1 if i < j else 0, n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


3987421
2876543


        