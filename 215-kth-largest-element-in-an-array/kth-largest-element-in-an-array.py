class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def helper(start, end, k):
            if start >= end:
                return None
                
            left, right = start, end
            pivot = nums[(left + right) // 2]

            while left <= right:
                while left <= right and nums[left] < pivot:
                    left += 1
                while left <= right and nums[right] > pivot:
                    right -= 1
                
                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
            
            if k <= right:
                helper(start, right, k)
            if k >= left:
                helper(left, end, k)
        # [0, 1, 2, 3, 4] => 1, 5 - 1
        helper(0, len(nums) - 1, len(nums) - k)
        # print(nums, len(nums) - 1)
        return nums[len(nums) - k]