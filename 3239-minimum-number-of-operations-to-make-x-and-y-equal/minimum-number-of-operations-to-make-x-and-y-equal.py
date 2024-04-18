class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        queue = deque([x])
        visited = set([x])
        res = -1

        while queue:
            res += 1
            for _ in range(len(queue)):
                node = queue.popleft()

                if node == y:
                    return res
                
                potential = [node + 1]

                if node > y:
                    potential += [node - 1]

                    if node % 11 == 0:
                        potential += [node // 11]
                    if node % 5 == 0:
                        potential += [node // 5]

                for nxt in potential:
                    if nxt in visited:
                        continue
                    visited.add(nxt)
                    queue.append(nxt)
        return -1
        