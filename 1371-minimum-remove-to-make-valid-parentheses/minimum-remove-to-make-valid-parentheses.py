class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        opened = []

        for i in range(len(s)):
            if s[i] == "(":
                opened += [i]
            elif s[i] == ")":
                if not opened:
                    s[i] = "#"
                else:
                    opened.pop()
        
        for i in opened[::-1]:
            s[i] = "#"
        
        return "".join(s).replace("#", "")