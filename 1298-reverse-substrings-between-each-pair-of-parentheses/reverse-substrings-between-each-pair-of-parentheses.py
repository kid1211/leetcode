class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = []

        for l in s:
            if l == "(":
                res += [""]
                tmp = ""
            elif l == ")":
                last = res.pop()
                tmp = last[::-1]
            else:
                tmp = l

            if not res:
                res += [tmp]
            else:
                res[-1] += tmp
        return res[-1]