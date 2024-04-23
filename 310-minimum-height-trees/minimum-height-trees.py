class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        neighbors = [set() for i in range(n)]

        for a, b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a)

        queue = deque([i for i in range(n) if len(neighbors[i]) == 1])
        print(queue)

        while n > 2:
            n -= len(queue)
            for _ in range(len(queue)):
                node = queue.popleft()

                for neighbor in neighbors[node]:
                    neighbors[neighbor].remove(node)

                    if len(neighbors[neighbor]) == 1:
                        queue.append(neighbor)

        return queue