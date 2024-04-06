# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        last = None
        res = None
        def dfs(node):
            nonlocal last, res
            if not node:
                return
            
            dfs(node.left)
            if last == p and not res:
                res = node
                return
            last = node
            dfs(node.right)
        dfs(root)
        return res