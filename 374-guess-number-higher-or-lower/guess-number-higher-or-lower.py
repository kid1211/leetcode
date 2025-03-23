# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left + 1 < right:
            mid = (left + right) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res < 0:
                right = mid
            else:
                left = mid

        return left if guess(left) == 0 else right