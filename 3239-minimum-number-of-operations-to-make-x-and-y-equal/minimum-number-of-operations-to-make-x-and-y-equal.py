class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        queue = deque([x])
        visited = set([x])
        res = -1
        while queue:
            res += 1
            for _ in range(len(queue)):
                num = queue.popleft()

                if num == y:
                    return res

                if num - 1 not in visited and num > y:
                    visited.add(num - 1)
                    queue.append(num - 1)
                if num + 1 not in visited:
                    visited.add(num + 1)
                    queue.append(num + 1)
                if num % 5 == 0 and num // 5 not in visited and num > y:
                    visited.add(num // 5)
                    queue.append(num // 5)
                if num % 11 == 0 and num // 11 not in visited and num > y:
                    visited.add(num // 11)
                    queue.append(num // 11)
        return -1
