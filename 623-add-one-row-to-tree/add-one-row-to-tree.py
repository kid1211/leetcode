# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def dfs(node, parent, currDepth):
            if currDepth == depth:
                if parent.left == node:
                    parent.left = TreeNode(val=val, left=node)
                elif parent.right == node:
                    parent.right = TreeNode(val=val, right=node)
                return
            if not node:
                return
            
            dfs(node.left, node, currDepth + 1)
            dfs(node.right, node, currDepth + 1)
        
        if depth == 1:
            return TreeNode(val=val, left = root)
        dfs(root, None, 1)
        return root
# 2 4
# 6 4