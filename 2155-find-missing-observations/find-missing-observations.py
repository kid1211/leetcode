class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = sum(rolls)
        remain = mean * (n + len(rolls)) - total

        if not (1 <= remain/n <= 6):
            return []
        
        res = []
        while remain:
            remainSlotFilledWithOne = n - 1
            val = min(6, remain - remainSlotFilledWithOne)

            remain -= val
            n -= 1
            res += [val]
        
        return res