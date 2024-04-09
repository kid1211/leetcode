class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        curr_total = sum(rolls)
        total = (len(rolls) + n) * mean

        remain = total - curr_total
        if not (1 <= remain / n <= 6):
            return []

        res = []
        for i in range(n):
            val = min(6, remain - (n - i - 1))
            res += [val]
            remain -= val
        return res