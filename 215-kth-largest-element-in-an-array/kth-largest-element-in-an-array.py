class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quick(start, end):
            if end <= start:
                return
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
                quick(start, right)
            elif k >= left:
                quick(left, end)
        
        quick(0, len(nums) - 1)
        return nums[k]
            

