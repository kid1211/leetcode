class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        rolling = res = 0

        for num in gain:
            rolling += num
            res = max(res, rolling)
        return res