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

            # print(leftIdx, rightIdx, left, right)
            if left and right:
                v1 = int(left)
                v2 = int(right)
                # print('ans', v1, v2)
                if v1 < v2:
                    return -1
                elif v1 > v2:
                    return 1
            else:
                break

        print('end', leftIdx, rightIdx)
        while left:
            if int(left) != 0:
                return 1
            left, leftIdx = getNext(version1, leftIdx)
    
        while right:
            if int(right) != 0:
                return -1
            right, rightIdx = getNext(version2, rightIdx)

        return 0
            