class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dfs(i, bal):
            if i == len(s):
                print(bal)
                return bal == 0

            if s[i] == "*":
                return (
                    dfs(i + 1, bal + 1) or 
                    dfs(i + 1, bal) or 
                    bal > 0 and dfs(i + 1, bal - 1)
                    )
            else:
                if s[i] == "(":
                    return dfs(i + 1, bal + 1)
                elif s[i] == ")" and bal > 0:
                    return dfs(i + 1, bal - 1)
                else:
                    return False
        
        return dfs(0, 0)
