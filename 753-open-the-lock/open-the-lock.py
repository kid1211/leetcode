class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque(["0000"])
        visited = set(deadends)
        if "0000" in visited:
            return -1
        visited.add("0000")

        res = -1
        while queue:
            res += 1
            for _ in range(len(queue)):
                node = queue.popleft()

                if node == target:
                    return res

                for i in range(len(node)):
                    nxtChar1 = str((int(node[i]) + 1) % 10)
                    nxtChar2 = str((int(node[i]) - 1) % 10)
                    nxt1 = node[:i] + nxtChar1 + node[i + 1:]
                    nxt2 = node[:i] + nxtChar2 + node[i + 1:]

                    print(node, nxt1, nxt2)
                    if nxt1 not in visited:
                        visited.add(nxt1)
                        queue.append(nxt1)
                    if nxt2 not in visited:
                        visited.add(nxt2)
                        queue.append(nxt2)

        return -1