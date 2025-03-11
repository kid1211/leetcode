class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for l in s:
            if l != '*':
                stack += [l]
            else:
                stack.pop()
        return "".join(stack)