class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @cache
        def dfs(ringId, keyId):
            # It is guaranteed that key could always be spelled by rotating ring.
            if keyId >= len(key):
                return 0

            res = sys.maxsize
            for i in range(len(ring)):
                if not key[keyId] == ring[i]:
                    continue
                distance = min(
                    (i - ringId) % len(ring),
                    (ringId - i) % len(ring),
                )
                
                res = min(res, distance + dfs(i, keyId + 1))
            return res
            
        return dfs(0, 0) + len(key)
