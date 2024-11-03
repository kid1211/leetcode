class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s += s
        expected = actual = 0
        PRIME = 31

        def get(l):
            return ord(l) - ord('a')
        

        def add(val, l):
            val *= PRIME
            val += get(l)
            val %= sys.maxsize // PRIME
            return val

        
        for i in range(len(goal)):
            expected = add(expected, goal[i])
            actual = add(actual, s[i])
        
        coef = PRIME ** (len(goal) - 1)
        for i in range(len(goal), len(s)):
            if expected == actual:
                return True
            
            actual -= coef * get(s[i - len(goal)])
            actual = add(actual, s[i])
            
        return expected == actual
