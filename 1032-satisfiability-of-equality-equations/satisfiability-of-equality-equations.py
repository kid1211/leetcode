class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)

        for _ in range(2):
            for expr in equations:
                a, b = ord(expr[0]) - ord('a'), ord(expr[-1]) - ord('a')

                if expr[1] == "=":
                    uf.union(a, b)
                else:
                    if uf.find(a) == uf.find(b):
                        return False

        return True
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

        if fa == fb:
            return True
        else:
            self.father[fa] = fb
            self.size -= 1
            return False