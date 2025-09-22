class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)

        maxi = 0
        res = 0
        for key, val in counter.items():
            if val == maxi:
                res += val
            elif val > maxi:
                maxi = val
                res = val

        return res

