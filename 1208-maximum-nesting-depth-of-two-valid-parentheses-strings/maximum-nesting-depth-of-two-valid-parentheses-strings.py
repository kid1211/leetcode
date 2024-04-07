class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        n = len(seq)
        res = [0] * n

        stack = []
        belong = 0
        for i in range(n):
            if seq[i] == "(":
                stack += [i]
                belong = 1 - belong # hmm
            else:
                if not stack:
                    return [] # not valid VPS
                res[i] = belong
                res[stack.pop()] = belong
                belong = 1 - belong
        return res

            
