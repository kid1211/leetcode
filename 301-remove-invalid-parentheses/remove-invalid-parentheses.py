class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        queue = deque([s])
        visited = set([s])

        def isValid(txt):
            bal = 0
            for l in txt:
                if l == "(":
                    bal += 1
                elif l == ")":
                    bal -= 1
                    if bal < 0:
                        return False
            return bal == 0
        
        res = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if isValid(node):
                    res += [node]
                    continue
                
                for i in range(len(node)):
                    nxt = node[:i] + node[i + 1:]
                    if nxt not in visited:
                        visited.add(nxt)
                        queue += [nxt]

            if res:
                return res
        return res
