# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def traverseLeft(self, node):
        while node:
            self.stack += [node]
            node = node.left

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.traverseLeft(root)

    def next(self) -> int:
        top = self.stack[-1]

        if top.right:
            self.traverseLeft(top.right)
        else:
            node = self.stack.pop()
            while self.stack and self.stack[-1].right == node:
                node = self.stack.pop()
        print([item.val for item in self.stack])
        return top.val

    def hasNext(self) -> bool:
        return self.stack
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

