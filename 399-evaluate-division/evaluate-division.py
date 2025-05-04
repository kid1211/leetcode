ROUNDING = 6
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = defaultdict(set)
        calc = defaultdict(float)

        for i in range(len(equations)):
            a, b = equations[i]

            edges[a].add(b)
            edges[b].add(a)
            calc[(a, b)] = round(values[i], ROUNDING)
            calc[(b, a)] = round(1 / values[i], ROUNDING)

        # print(edges, calc)

        def dfs(start, end, visited):
            if (start, end) in calc:
                return calc[(start, end)]

            if start not in edges or end not in edges:
                return -1.0

            if start == end:
                return 1.0

            for nextNode in edges[start]:
                if nextNode in visited:
                    continue
                visited.add(nextNode)
                temp = dfs(nextNode, end, visited)
                visited.remove(nextNode)

                if temp == -1.0:
                    continue
                # print((start, end), ":", (temp, (nextNode, end)), (calc[(start, nextNode)], temp))
                return calc[(start, nextNode)] * temp
            return -1.0

        return [
            dfs(left, right, set([left])) for left, right in queries
        ]

# ('dd', 'a') : (-1.0, ('ee', 'a')) (9.0, -1.0)
# ('ff', 'a') : (-9.0, ('dd', 'a')) (0.333333, -9.0)