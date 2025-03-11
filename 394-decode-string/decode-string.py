class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for l in s:
            if l != "]":
                stack += [l]
            else:
                # write to stack
                tmp = ""
                while stack and stack[-1] != "[":
                    tmp += stack.pop()

                stack.pop()

                num = ""
                while stack and stack[-1].isnumeric():
                    num += stack.pop()

                for i in range(int(num[::-1])):
                    for l in reversed(tmp):
                        stack += [l]

                # print(tmp, num)
        return "".join(stack)