class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dfs(i, bal):
            if i == len(s):
                print(bal)
                return bal == 0

            if s[i] == "*":
                isValid = dfs(i + 1, bal + 1) or dfs(i + 1, bal)
                return isValid or bal > 0 and dfs(i + 1, bal - 1)
            else:
                if s[i] == "(":
                    return dfs(i + 1, bal + 1)
                elif s[i] == ")" and bal > 0:
                    return dfs(i + 1, bal - 1)
                else:
                    return False
        
        return dfs(0, 0)

# class Solution:
#     def checkValidString(self, s: str) -> bool:
#         @cache
#         def is_valid_string(index: int, open_count: int) -> bool:
#             if index == len(s):
#                 return open_count == 0

#             is_valid = False
#             if s[index] == '*':
#                 is_valid |= is_valid_string(index + 1, open_count + 1)  # Treat '*' as '('
#                 if open_count > 0:
#                     is_valid |= is_valid_string(index + 1, open_count - 1)  # Treat '*' as ')'
#                 is_valid |= is_valid_string(index + 1, open_count)  # Treat '*' as empty
#             else:
#                 # Handle '(' and ')'
#                 if s[index] == '(':
#                     is_valid = is_valid_string(index + 1, open_count + 1)  # Increment count for '('
#                 elif open_count > 0:
#                     is_valid = is_valid_string(index + 1, open_count - 1)  # Decrement count for ')'

#             # Memoize and return the result
#             # memo[index][open_count] = 1 if is_valid else 0
#             return is_valid
#         return is_valid_string(0, 0)
