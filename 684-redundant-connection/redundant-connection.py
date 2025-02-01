class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges) + 1)

        for left, right in edges:
            if uf.union(left, right) == False:
                return [left, right]
        return []

class UnionFind:
    def __init__(self, n):
        self.father = { i:i for i in range(n) }
    
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

        if fa == fb:
            return False
        
        self.father[fa] = fb
        return True
