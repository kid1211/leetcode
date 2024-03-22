# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        def isCelebrity(idx):
            for i in range(n):
                if i == idx:
                    continue
                if cachedKnow(i, idx) and not cachedKnow(idx, i):
                    continue
                return False
            return True
        
        @cache
        def cachedKnow(a, b):
            return knows(a, b)
        
        canadiate = 0
        for i in range(1, n):
            if cachedKnow(canadiate, i):
                canadiate = i
        
        return canadiate if isCelebrity(canadiate) else -1