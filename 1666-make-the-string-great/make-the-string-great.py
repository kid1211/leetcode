class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for l in s:
            if stack and stack[-1] != l and stack[-1].lower() == l.lower():
                stack.pop()
                continue
            stack.append(l)
        return "".join(stack)