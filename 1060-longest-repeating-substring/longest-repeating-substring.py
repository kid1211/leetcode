class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        PRIME = 31

        # def getChar(c):
        #     return ord(c) - ord('a')

        def add(hashVal, char):
            hashVal *= PRIME
            hashVal += ord(char)
            hashVal %= sys.maxsize // PRIME
            return hashVal

        def isRepeating(k):
            # assume k less than len(s)
            rolling = 0
            for i in range(k):
                rolling = add(rolling, s[i])
            
            visited = set([rolling])
            coef = PRIME ** (k - 1)
            for i in range(k, len(s)):
                rolling -= coef * ord(s[i - k])
                rolling = add(rolling, s[i])

                if rolling in visited:
                    return True
                visited.add(rolling)
            return False
        # print(isRepeating(2))
        # print(isRepeating(3))
        
        left, right = 1, len(s) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if isRepeating(mid):
                left = mid
            else:
                right = mid
        
        if isRepeating(right):
            return right
        elif isRepeating(left):
            return left
        else:
            return 0