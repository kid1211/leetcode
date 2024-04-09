"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        prev = None
        current = leaf
        def printing(node):
            res = str(node.val) + ": "
            if node.parent:
                res += f"parent->{node.parent.val}"
            if node.left:
                res += f"left->{node.left.val}"
            if node.right:
                res += f"right->{node.right.val}"
            print(res)
            node = node.left

        while current:
            print('before')
            printing(current)

            ori_parent = current.parent
            current.parent = prev
            
            print('after')
            printing(current)
            if current == root:
                break
    
            if current.left != prev:
                current.right = current.left
            current.left = ori_parent
    

            prev = current
            current = current.left
        
        if current.parent == current.left:
            current.left = None
        elif current.parent == current.right:
            current.right = None

        return leaf
# 7: left->2
# 2: parent->7left->5right->4
# 5: parent->2left->3right->6
# 3: parent->5right->1