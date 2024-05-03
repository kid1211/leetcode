class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        def getNext(text, start):
            end = 0
            for end in range(start, len(text)):
                if text[end] == ".":
                    break
            end += 1 if end == len(text) - 1 else 0
            return text[start:end], end + 1
    
        leftIdx = rightIdx = 0
        while True:
            left, leftIdx = getNext(version1, leftIdx)
            right, rightIdx = getNext(version2, rightIdx)

            if left and right:
                diff = int(left) - int(right)
                if diff < 0:
                    return -1
                elif diff > 0:
                    return 1
            else:
                break

        while left:
            if int(left) != 0:
                return 1
            left, leftIdx = getNext(version1, leftIdx)
    
        while right:
            if int(right) != 0:
                return -1
            right, rightIdx = getNext(version2, rightIdx)

        return 0
            