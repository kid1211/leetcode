# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(res, node):
            if not node:
                return res
            
            if not node.left and not node.right:
                return res + [node.val]
            
            left = dfs(res, node.left)
            right = dfs(res, node.right)
            return left + right
        
        return dfs([], root1) == dfs([], root2)