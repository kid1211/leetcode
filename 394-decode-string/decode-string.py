class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        def reversedString(s):
            res = ""
            for i in range(len(s) - 1, -1, -1):
                res += s[i]
            return res

        for l in s:
            if l != ']':
                stack += [l]
            else:
                reverse = ""
                while stack and stack[-1] != "[":
                    reverse += stack.pop()
                stack.pop() #pop [
                num = ""
                while stack and stack[-1].isnumeric():
                    num += stack.pop()

                for i in range(int(reversedString(num))):
                    for ans in reversedString(reverse):
                        stack += [ans]
        
        return "".join(stack)


