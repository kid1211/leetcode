# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def dfs(root):
            nonlocal res

            if not root:
                return root
            
            left = dfs(root.left)
            right = dfs(root.right)

            isPFound = root == p or left == p or right == p
            isQFound = root == q or left == q or right == q

            if isPFound and isQFound:
                res = root
                return root
            
            if left == p or left == q:
                return left
            if right == p or right == q:
                return right
            return root

        dfs(root)
        return res