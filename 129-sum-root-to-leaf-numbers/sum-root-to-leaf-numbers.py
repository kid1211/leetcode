# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, val):
            nonlocal res
            if not node:
                return
            val *= 10
            val += node.val
            if not node.left and not node.right:
                res += val
                return
            dfs(node.left, val)
            dfs(node.right, val)
        
        dfs(root, 0)
        return res