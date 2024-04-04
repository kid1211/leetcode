class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        res = bal = 0
        
        for l in s:
            if l == "(":
                bal += 1
            elif l == ")":
                res = max(res, bal)
                bal -= 1
        return res