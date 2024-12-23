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

            nodeSet = set([root, left ,right])

            if p in nodeSet and q in nodeSet:
                res = root
                return root

            if p == left or q == left:
                return left
            if p == right or q == right:
                return right
            return root
        
        dfs(root)
        return res
        