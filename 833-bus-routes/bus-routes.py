class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        n = len(routes)
        busPath = { i: set(routes[i]) for i in range(len(routes)) }
        busPath[-1] = set([source])

        edges = defaultdict(set)
        for i in range(n):
            if source in busPath[i]:
                edges[-1].add(i)
            for j in range(i + 1, n):
                if busPath[i].intersection(busPath[j]):
                    edges[i].add(j)
                    edges[j].add(i)
        # print(edges)
        queue = deque([-1])
        visited = set([-1])
        res = -1

        while queue:
            # print(queue)
            res += 1
            for _ in range(len(queue)):
                route = queue.popleft()

                if target in busPath[route]:
                    return res
                
                for nxtRoute in edges[route]:
                    if nxtRoute in visited:
                        continue
                    visited.add(nxtRoute)
                    queue.append(nxtRoute)
                    
        return -1

# 37 -> 43
# [
#     0[10,13,22,28,32,35,*43*],
#     1[2,11,15,25,27],
#     2[6,13,18,25,42],
#     3[5,6,20,27,*37*,47],
#     4[7,11,19,23,35],
#     5[7,11,17,25,31,*43*,46,48],
#     6[1,4,10,16,25,26,46],
#     7[7,11],
#     8[3,9,19,20,21,24,32,45,46,49],
#     9[11,41]]