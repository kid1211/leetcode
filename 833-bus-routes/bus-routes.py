class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        n = len(routes)
        busPath = { i:set(routes[i]) for i in range(n) }
        busPath[-1] = set([source])
        edges = defaultdict(set)

        for i in range(n):
            if source in busPath[i]:
                edges[-1].add(i)
            for j in range(i + 1, n):
                if busPath[i].intersection(busPath[j]):
                    edges[i].add(j)
                    edges[j].add(i)
        
        res = -1
        queue = deque([-1])
        visited = set([-1])

        while queue:
            res += 1
            for _ in range(len(queue)):
                bus = queue.popleft()

                if target in busPath[bus]:
                    return res
                
                for nxtRoute in edges[bus]:
                    if nxtRoute not in visited:
                        visited.add(nxtRoute)
                        queue += [nxtRoute]
        return -1