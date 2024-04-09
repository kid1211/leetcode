# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    largest = -sys.maxsize + 1
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if not self.isValidBST(root.left):
            return False
        
        if self.largest >= root.val:
            return False
        self.largest = root.val
        
        return self.isValidBST(root.right)