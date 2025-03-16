# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        maxVal, maxLevel = root.val, 1
        currLevel = 1
        while queue:
            curr = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                curr += node.val

                if node.left:
                    queue += [node.left]
                if node.right:
                    queue += [node.right]
            
            if curr > maxVal:
                maxVal = curr
                maxLevel = currLevel
            currLevel += 1
        return maxLevel