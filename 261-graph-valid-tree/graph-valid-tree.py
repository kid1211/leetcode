class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False

        uf = UnionFind(n)
        for a, b in edges:
            if not uf.union(a, b):
                return False
        return True

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
            return True
        else:
            return False