class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        sameTime = defaultdict(list)

        for p1, p2, t in meetings:
            sameTime[t] += [(p1, p2)]
        
        uf = UnionFind(n)
        uf.union(0, firstPerson)
        for t in sorted(sameTime.keys()):
            sameTimeMeeting = sameTime[t]

            for p1, p2 in sameTimeMeeting:
                uf.union(p1, p2)
            
            for p1, p2 in sameTimeMeeting:
                if uf.find(p1) == uf.find(0) or uf.find(p2) == uf.find(0):
                    continue
                uf.reset(p1)
                uf.reset(p2)
        
        return [i for i in range(n) if uf.find(i) == uf.find(0)]

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

        if fa != fb:
            self.father[fa] = fb
    def reset(self, node):
        self.father[node] = node