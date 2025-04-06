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
            dfs(node.right if isLeft else node.left, isLeft, 1)

        dfs(root, True, 0)
        return res

# class Solution:
#     def longestZigZag(self, root: Optional[TreeNode]) -> int:

#         def dfs(node, isLeft):
#             if not node:
#                 return 0

#             return max(
#                 1 + dfs(node.left if isLeft else node.right, not isLeft),
#                 dfs(node.right if isLeft else node.left, isLeft)
#             )


#         return max(
#             dfs(root, True),
#             dfs(root, False)
#         ) - 1