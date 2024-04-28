class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * N
        ans = [0] * N
        def dfs(node = 0, parent = None):
            for child in graph[node]:
                if child == parent:
                    # print(child, parent)
                    continue
                dfs(child, node)
                count[node] += count[child]
                ans[node] += ans[child] + count[child]

        def dfs2(node = 0, parent = None):
            # print(node, parent, ans)
            for child in graph[node]:
                if child == parent:
                    continue
                # node is the parent
                ans[child] = ans[node] - count[child] + N - count[child]
                dfs2(child, node)

        dfs()
        # print(count, ans)
        dfs2()
        # print(count, ans)
        return ans