class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        edges = defaultdict(list)
        n = len(parent)
        for i in range(n):
            edges[parent[i]] += [i]
        
        res = 0
        def dfs(curr):
            nonlocal res
            
            longest = secondLongest = 0
            for child in edges[curr]:
                longestChain = dfs(child)

                if s[curr] == s[child]:
                    continue
                
                if longestChain > longest:
                    longest, secondLongest = longestChain, longest
                elif longestChain > secondLongest:
                    secondLongest = longestChain
                
            res = max(res, longest + secondLongest + 1)
            return longest + 1
        
        dfs(edges[-1][0])
        return res