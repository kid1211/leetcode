class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set([0])
        edges = defaultdict(list)
        res = 0
        for left, right in connections:
            edges[left] += [(right, (left, right))]
            edges[right] += [(left, (left, right))]


        def dfs(parent):
            nonlocal res

            # no optimize, when the next chilrend is already there so hmm
            for nextNode, direction in edges[parent]:
                if nextNode in visited:
                    continue
                # print(direction, (nextNode, parent))
                if direction != (nextNode, parent):
                    res += 1

                visited.add(nextNode)
                dfs(nextNode)
        
        dfs(0)
        return res
