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
                return None

            left = dfs(root.left)
            right = dfs(root.right)

            nodeSet = set([root, left, right])

            if p in nodeSet and q in nodeSet:
                res = root
                return root
            
            if left == p or left == q:
                return left
            if right == p or right == q:
                return right
            if root == p or root == q:
                return root
            return None
            
        dfs(root)
        return res