class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = (len(nums)) // 2
        leftSorted = self.sortArray(nums[:mid])
        rightSorted = self.sortArray(nums[mid:])

        res = []
        left = right = 0
        leftN, rightN = len(leftSorted), len(rightSorted)

        while left < leftN or right < rightN:
            leftVal = leftSorted[left] if left < leftN else sys.maxsize
            rightVal = rightSorted[right] if right < rightN else sys.maxsize

            if leftVal < rightVal:
                res += [leftSorted[left]]
                left += 1
            else:
                res += [rightSorted[right]]
                right += 1
        
        return res