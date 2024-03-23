class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
            # print(fast, slow)
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow

# [2,5,9,6,9,3,8,9,7,1]
#  0 1 2 3 4 5 6 7 8 9
#    s               f
#  0 1 2 3 4 5 6 7 8 9
#    f       s       
#  0 1 2 3 4 5 6 7 8 9
#    f       s       