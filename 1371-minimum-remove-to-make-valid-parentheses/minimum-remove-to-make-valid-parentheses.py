class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        skip = set()
        for i in range(len(s)):
            if s[i] == "(":
                stack += [i]
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    skip.add(i)
        
        for item in stack:
            skip.add(item)
        
        return "".join([s[i] for i in range(len(s)) if i not in skip])