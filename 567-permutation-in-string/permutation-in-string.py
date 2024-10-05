class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash1, hash2 = defaultdict(int), defaultdict(int)
        k = len(s1)

        if k > len(s2):
            return False
        
        for i in range(k):
            hash1[s1[i]] += 1
            hash2[s2[i]] += 1
        
        for i in range(k, len(s2)):
            if hash1 == hash2:
                return True
            
            hash2[s2[i]] += 1
            hash2[s2[i - k]] -= 1
            if hash2[s2[i - k]] == 0:
                del hash2[s2[i - k]]
        
        return hash1 == hash2
            
