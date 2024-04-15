# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node, hasSibling):
            nonlocal res
            if not node:
                return
            
            dfs(node.left, node.right is not None)
            dfs(node.right, node.left is not None)

            if not hasSibling:
                res += [node.val]
        
        dfs(root, True) # root doesn't have sibling, but to save one line
        return res