# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        @cache
        def cachedKnow(a, b):
            return knows(a, b)

        def isCelebrity(idx):
            for i in range(n):
                if i == idx:
                    continue
                if cachedKnow(idx, i) or not cachedKnow(i, idx):
                    return False
            return True
        
        potential = 0
        for i in range(1, n):
            if cachedKnow(potential, i):
                potential = i
        
        return potential if isCelebrity(potential) else -1