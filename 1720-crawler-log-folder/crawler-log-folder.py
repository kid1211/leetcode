class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            action = log.split("/")[0]

            if action == ".":
                continue
            elif action == "..":
                depth -= 1 if depth > 0 else 0
            else:
                depth += 1
        return depth