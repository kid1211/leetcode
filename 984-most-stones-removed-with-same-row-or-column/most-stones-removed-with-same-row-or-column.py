class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # dfs, try remove, this row, put it back, 
        
        # unionFind, n - component, is how many you can removed
        # connect them if they have the same row, or some column
        # exit criteria, when no 
        uf = UnionFind(len(stones))
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)
        return len(stones) - uf.size

class UnionFind:
    def __init__(self, n):
        self.father = {i:i for i in range(n)}
        self.size = n
    
    def find(self, node):
        path = []
        while node != self.father[node]:
            path += [node]
            node = self.father[node]
        for child in path:
            self.father[child] = node
        return node
    
    def union(self, a, b):
        fa, fb = self.find(a), self.find(b)

        if fa != fb:
            self.size -= 1
            self.father[fa] = fb
            return True
        else:
            return False