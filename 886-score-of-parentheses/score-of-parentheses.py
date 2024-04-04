class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        bal = res = 0
        reset = True
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