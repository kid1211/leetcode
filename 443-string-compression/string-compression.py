class Solution:
    def compress(self, chars: List[str]) -> int:
        # edge
        def writeAns(char, length):
            nonlocal left
            if not char:
                return
            # if length == 1:
            #     chars[left] = char
            #     left += 1
            #     return

            for d in [char] + list(str(length)):
                chars[left] = d
                left += 1

                if length == 1:
                    return

        lastChar = None
        lastLength = 0
        left = 0
        chars += " "
        for right in range(len(chars)):
            if lastChar == chars[right]:
                lastLength += 1
                continue
            writeAns(lastChar, lastLength)
            lastChar = chars[right]
            lastLength = 1

        return left


# left spot for writing,
# right point ,gooing until see a different chrater

# write to left, keep going.