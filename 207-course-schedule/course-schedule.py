class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = { i:0 for i in range(numCourses) }
        edges = defaultdict(list)

        for post, pre in prerequisites:
            edges[pre] += [post]
            indegree[post] += 1
        
        queue = deque([i for i in indegree if indegree[i] == 0])
        res = []
        while queue:
            node = queue.popleft()
            res += [node]

            for nxt in edges[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue += [nxt]
        return len(res) == numCourses
            