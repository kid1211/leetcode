class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = bal = 0
        reset = False
        for l in s:
            if l == "(":
                bal += 1
                reset = True
            elif l == ")":
                bal -= 1
                if reset:
                    res += 2 ** bal
                    reset = False
        return res

