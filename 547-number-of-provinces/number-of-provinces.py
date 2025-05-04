class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        for row in range(n):
            for col in range(row + 1, n):
                if isConnected[row][col] == 1:
                    uf.union(row, col)
        
        return uf.isConnected

class UnionFind:
    def __init__(self, n):
        self.father = { i: i for i in range(n) }
        self.isConnected = n

    def find(self, node):
        path = []
        while node != self.father[node]:
            path += [node]
            node = self.father[node]

        for item in path:
            self.father[item] = node

        return node

    def union(self, a, b):
        fa, fb = self.find(a), self.find(b)

        if fa != fb:
            self.father[fa] = fb
            # You can optimize
            self.isConnected -= 1