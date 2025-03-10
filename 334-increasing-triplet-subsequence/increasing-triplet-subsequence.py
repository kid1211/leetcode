class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = j = + sys.maxsize

        for num in nums:
            # print("before:", i, j, k, num)
            if num <= i:
                i = num
            elif num <= j:
                j = num

            else:
                return True
            # print("after:", i, j, k, num)
        return False
