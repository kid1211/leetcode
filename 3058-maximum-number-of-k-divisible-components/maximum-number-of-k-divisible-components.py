class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:   
        adj = defaultdict(list)
        for a, b in edges:
            adj[a] += [b]
            adj[b] += [a]

        res = 0
        def dfs(curr, parent):
            nonlocal res

            sums = values[curr]

            for neighbor in adj[curr]:
                if neighbor == parent:
                    continue
                sums += dfs(neighbor, curr)
                sums %= k

            sums %= k
            if sums == 0:
                res += 1
            
            return sums
        
        dfs(0, -1)
        return res