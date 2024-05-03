class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        def getNext(text, start):
            # if text[start] == ".":
            #     start += 1
            end = 0
            for end in range(start, len(text)):
                if text[end] == ".":
                    break
            end += 1 if end == len(text) - 1 else 0
            return text[start:end]
    
        leftIdx = rightIdx = 0
        while True:
            left = getNext(version1, leftIdx)
            right = getNext(version2, rightIdx)

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
                
            leftIdx += len(left) + 1
            rightIdx += len(right) + 1
        
        while left and leftIdx < len(version1):
            left = getNext(version1, leftIdx)
            if left and int(left) != 0:
                return 1
            leftIdx += len(left) + 1
    
        while right and rightIdx < len(version2):
            right = getNext(version2, rightIdx)
            if right and int(right) != 0:
                return -1
            rightIdx += len(right) + 1
            
        return 0
            