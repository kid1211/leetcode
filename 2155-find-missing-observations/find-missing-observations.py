class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = sum(rolls)
        remain = mean * (n + len(rolls)) - total

        if not (1 <= remain/n <= 6):
            return []
        print(remain, n)
        # [6, 6, 6, 1, 1]
        # 12 + 15
        res = []

        while remain:
            # n - len(res) == remain slot if filled all 1
            val = min(6, remain - (n - len(res) - 1))
            remain -= val
            res += [val]
        
        return res
# 3
# 3 - 2

# 12/2 
# 6, 6
# 9 - 6 = 3, < 2 - 1 - 1