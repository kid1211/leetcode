# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        # if len(preorder) == 2:
        #     left = TreeNode(preorder[1])
        #     return TreeNode(preorder[0], left)

        leftChildLen = None
        for i in range(len(postorder) - 1):
            if postorder[i] == preorder[1]:
                leftChildLen = i + 1

        if leftChildLen is None:
            print('should never happen', preorder, leftChildLen)
            return None
        left = self.constructFromPrePost(
            preorder[1:leftChildLen + 1],
            postorder[:leftChildLen]
        )
        right = self.constructFromPrePost(
            preorder[1 + leftChildLen:], 
            postorder[leftChildLen:len(postorder) - 1]
        )
        return TreeNode(preorder[0], left, right)
# [2,1,3]
# [3,1,2] only if 1, 3, 2

# [2,1,null,3]