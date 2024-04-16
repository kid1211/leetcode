class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        bal = defaultdict(int)

        for a, b, amount in transactions:
            bal[a] += amount
            bal[b] -= amount
        
        val = [item for item in bal.values() if item != 0]
        
        def dfs(curr):
            while curr < len(val) and val[curr] == 0:
                curr += 1
    
            if curr == len(val):
                return 0
            
            res = sys.maxsize
            for nxt in range(curr + 1, len(val)):
                if val[nxt] * val[curr] < 0:
                    val[nxt] += val[curr]
                    # val[curr] -= val[nxt]
                    res = min(res, 1 + dfs(curr + 1))
                    val[nxt] -= val[curr]
                    # val[curr] += val[nxt]
            return res
        return dfs(0)