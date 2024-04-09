class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        longestPath = 1
        n = len(parent)
        children = defaultdict(list)

        for i in range(1, n):
            children[parent[i]] += [i]

        def dfs(currentNode):
            nonlocal longestPath
            if currentNode not in children:
                return 1
            longestChain = secondLongestchain = 0
            for child in children[currentNode]:
                longestChainStartingFromChild = dfs(child)

                if s[currentNode] == s[child]:
                    continue
                
                if longestChainStartingFromChild > longestChain:
                    secondLongestchain = longestChain
                    longestChain = longestChainStartingFromChild
                elif longestChainStartingFromChild > secondLongestchain:
                    secondLongestchain = longestChainStartingFromChild
            longestPath = max(longestPath, longestChain + secondLongestchain + 1)
            return longestChain + 1

        dfs(0)
        return longestPath

# defaultdict(<class 'list'>, {-1: [0], 0: [1, 2, 3]})
# defaultdict(<class 'list'>, {-1: [0], 0: [1, 2], 1: [3, 4], 2: [5]})