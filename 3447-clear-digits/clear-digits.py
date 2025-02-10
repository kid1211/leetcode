class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for l in s:
            if l.isdigit():
                if stack:
                    stack.pop()
            else:
                stack += [l]
        
        return "".join(stack)