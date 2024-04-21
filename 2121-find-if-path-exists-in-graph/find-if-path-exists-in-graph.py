class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)

        for x, y in edges:
            uf.union(x, y)
        
        return uf.find(source) == uf.find(destination)

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

        if fa != fb:
            self.father[fa] = fb