class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        indegree = {}
        edges = defaultdict(list)

        for i in range(len(recipes)):
            indegree[recipes[i]] = 0
            for item in ingredients[i]:
                if item not in supplies:
                    indegree[recipes[i]] += 1
                    edges[item] += [recipes[i]]
        
        queue = deque([item for item in indegree if indegree[item] == 0])
        res = []

        while queue:
            node = queue.popleft()
            if node not in supplies:
                res += [node]
            
            for nextNode in edges[node]:
                indegree[nextNode] -= 1
                if indegree[nextNode] == 0:
                    queue.append(nextNode)
        return res