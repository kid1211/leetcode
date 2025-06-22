class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for l in s:
            if l in maps:
                stack += [l]
                continue
            
            if not stack or maps[stack[-1]] != l:
                return False
            else:
                stack.pop()
        return len(stack) == 0