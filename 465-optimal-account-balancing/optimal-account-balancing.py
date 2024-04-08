class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = collections.defaultdict(int)

        for a, b, amount in transactions:
            balance[a] -= amount
            balance[b] += amount

        vals = [val for val in balance.values() if val != 0]
        
        # @cache
        def dfs(curr):
            while curr < len(vals) and vals[curr] == 0:
                curr += 1
            if curr == len(vals):
                return 0

            res = sys.maxsize
            for nxt in range(curr + 1, len(vals)):
                if vals[nxt] * vals[curr] < 0:
                    vals[nxt] += vals[curr]
                    res = min(res, 1 + dfs(curr + 1))
                    vals[nxt] -= vals[curr]
            return res
        return dfs(0)