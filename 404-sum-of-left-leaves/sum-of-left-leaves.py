# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, isLeft):
            nonlocal res
            if not node:
                return
            
            dfs(node.left, True)
            if isLeft and not node.right and not node.left:
                res += node.val
            dfs(node.right, False)
        
        dfs(root, False)
        return res