class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for a, b in edges:
            uf.union(a, b)
        # print(uf.father)
        # print(uf.rank)
        return uf.connected
    
class UnionFind:
    def __init__(self, n):
        self.father = { i: i for i in range(n) }
        self.rank = { i: 1 for i in range(n) }
        self.connected = n
    
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
            return
        self.connected -= 1

        if self.rank[fa] < self.rank[fb]:
            self.rank[fa] += 1
            self.father[fa] = fb
        elif self.rank[fa] < self.rank[fb]:
            self.father[fa] = fb
        else:
            self.father[fb] = fa
