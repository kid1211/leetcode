class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = collections.defaultdict(int)

        for a, b, amount in transactions:
            balance[a] -= amount # wtf
            balance[b] += amount
        
        unsettled = [val for val in balance.values() if val != 0]

        def dfs(curr):
            while curr < len(unsettled) and unsettled[curr] == 0:
                curr += 1
            
            if curr == len(unsettled):
                return 0
            
            res = sys.maxsize
            for nxt in range(curr + 1, len(unsettled)):
                if unsettled[curr] * unsettled[nxt] < 0:
                    delta_ratio = 1 # -1 if unsettled[nxt] > 0 else 1
                    unsettled[nxt] += delta_ratio * unsettled[curr]
                    res = min(res, 1 + dfs(curr + 1))
                    unsettled[nxt] -= delta_ratio * unsettled[curr]
            return res
        return dfs(0)