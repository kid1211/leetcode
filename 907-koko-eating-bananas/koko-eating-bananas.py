class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def getTime(speed):
            res = 0

            for item in piles:
                res += ceil(item / speed)
            return res

        left, right = 1, max(piles)

        while left + 1 < right:
            mid = (left + right) // 2

            if getTime(mid) > h:
                left = mid
            else:
                right = mid
        # print(left, right)
        return left if getTime(left) <= h else right