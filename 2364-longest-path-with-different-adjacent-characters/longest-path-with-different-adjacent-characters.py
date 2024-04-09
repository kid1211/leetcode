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
                chain = dfs(child)

                if s[curr] == s[child]:
                    continue
                
                if chain > longest:
                    longest, secondLongest = chain, longest
                elif chain > secondLongest:
                    secondLongest = chain
                
            res = max(res, longest + secondLongest + 1)
            return longest + 1
        
        dfs(edges[-1][0])
        return res