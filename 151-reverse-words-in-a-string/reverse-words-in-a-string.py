class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)

        def reverse(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        
        def move(start, move_amount):
            nonlocal s
            i = start
            for j in range(start + move_amount, len(s)):
                s[i] = s[j]
                i += 1

            # print(start, move_amount, s, i)
            s = s[:i]
        
        def stripHead():
            for i in range(len(s)):
                if s[i] != " ":
                    move(0, i)
                    return

        stripHead()
        reverse(0, len(s) - 1)
        stripHead()

        s += " "
        lastSpace = 0
        for i in range(len(s)):
            if s[i] != " ":
                continue

            reverse(lastSpace, i - 1)
            lastSpace = i + 1

        left = 0
        while left < len(s):
            if s[left] != " " or s[left - 1] != " ":
                left += 1
                continue
            
            moveForward = 0
            while left + moveForward < len(s) and s[left + moveForward] == " ":
                moveForward += 1
            # print(left, moveForward)
            move(left, moveForward)
            # break
            # print("yolog", left, moveForward)
            left += 1

        return "".join(s)[:-1]