# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == key:
            if root.left and root.right:
                smallest = root.right
                while smallest.left:
                    smallest = smallest.left
                
                root.val = smallest.val
                root.right = self.deleteNode(root.right, smallest.val)
                return root
            else:
                return root.left or root.right
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        
        return root