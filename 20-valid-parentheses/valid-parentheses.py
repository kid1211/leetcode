class Solution:
    def isValid(self, s: str) -> bool:
        # mapping = {
        #     "(": ")",
        #     "[": "]",
        #     "{": "}"
        # }
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for l in s:
            if l in mapping:
                if stack and stack[-1] == mapping[l]:
                    stack.pop()
                else:
                    return False
            else:
                stack += [l]
        return not stack