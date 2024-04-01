class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h = defaultdict(int)
        h[0] = 1
        res = rolling = 0
        for num in nums:
            rolling += num
            res += h[rolling - k]
            h[rolling] += 1
        return res