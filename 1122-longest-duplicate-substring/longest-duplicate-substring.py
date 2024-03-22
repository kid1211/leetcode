class Solution:
    def longestDupSubstring(self, s: str) -> str:
        PRIME = 211
        @cache
        def addValue(i, hashVal):
            hashVal *= PRIME
            hashVal += ord(s[i])
            hashVal %= sys.maxsize // PRIME
            return hashVal

        @cache
        def checkAnswer(k):
            rolling = 0

            for i in range(k):
                rolling = addValue(i, rolling)
            
            coef = PRIME ** (k - 1) % (sys.maxsize // PRIME)
            unique = set([rolling])

            for i in range(k, len(s)):
                rolling -= coef * ord(s[i - k])
                rolling = addValue(i, rolling)

                if rolling in unique:
                    return i - k + 1
                unique.add(rolling)
            
            return -1
        
        left, right = 1, len(s) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if checkAnswer(mid) != -1:
                left = mid
            else:
                right = mid
        
        tmp_left = checkAnswer(left)
        tmp_right = checkAnswer(right)
        
        if tmp_right != -1:
            return s[tmp_right:tmp_right + right]
        elif tmp_left != -1:
            return s[tmp_left:tmp_left + left]
        else:
            return ""


        


