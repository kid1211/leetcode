# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, isLeft, step):
            nonlocal res
            if not node:
                return
            res = max(res, step)

            dfs(node.left if isLeft else node.right, not isLeft, step + 1)
            if isLeft:
                # dfs(node.left, False, step + 1)
                dfs(node.right, True, 1)
            else:
                dfs(node.left, False, 1)
                # dfs(node.right, True, step + 1)

        dfs(root, True, 0)
        return res

# class Solution:
#     def longestZigZag(self, root: Optional[TreeNode]) -> int:
#         self.pathLength = 0
        
#         def dfs(node, goLeft, steps):
#             if not node:
#                 return

#             self.pathLength = max(self.pathLength, steps)
#             if goLeft:
#                 dfs(node.left, False, steps + 1)
#                 dfs(node.right, True, 1)
#             else:
#                 # dfs(node.left, False, 1)
#                 dfs(node.right, True, steps + 1)
        
#         dfs(root, True, 0)
#         dfs(root, False, 0)
#         return self.pathLength