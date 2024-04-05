class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        same_time = defaultdict(list)
        for p1, p2, time in meetings:
            same_time[time] += [(p1, p2)]
        # 0 and first person knows it
        uf = UnionFind(n)
        uf.union(0, firstPerson)

        for time in sorted(same_time.keys()):
            for p1, p2 in same_time[time]:
                uf.union(p1, p2)
            
            for p1, p2 in same_time[time]:
                if uf.find(p1) == uf.find(0) or uf.find(p1) == uf.find(0):
                    continue
                uf.reset(p1)
                uf.reset(p2)
            
        res = []
        for i in range(n):
            if uf.find(i) == uf.find(0):
                res += [i]
        return res

class UnionFind:
    def __init__(self, n):
        self.father = {i:i for i in range(n)}
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
        else:
            self.father[fb] = fa
            return True
    def reset(self, a):
        self.father[a] = a
