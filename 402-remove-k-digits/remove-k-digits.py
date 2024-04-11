class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for d in num:
            while k and stack and d < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(d)
        res = stack[:-k] if k else stack
        return "".join(res).lstrip('0') or '0'