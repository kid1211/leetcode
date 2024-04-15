class Solution:
    def findLatestTime(self, s: str) -> str:
        
        def isValid(expected, actual):
            for i in range(len(expected)):
                if expected[i] == actual[i] or expected[i] == '?':
                    continue
                return False
            return True

        for hour in range(11, -1, -1):
            hr = ('0' + str(hour))[-2:]

            if isValid(s[:2], hr):
                break
    
        for hour in range(59, -1, -1):
            mm = ('0' + str(hour))[-2:]

            if isValid(s[-2:], mm):
                break
        
        return hr + ':' + mm