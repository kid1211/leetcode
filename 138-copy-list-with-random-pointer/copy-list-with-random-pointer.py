"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old2New = {}
        node = head

        while node:
            old2New[node] = Node(node.val)
            node = node.next
        
        node = head
        while node:
            newNode = old2New[node]

            newNode.next = old2New[node.next] if node.next else None
            newNode.random = old2New[node.random] if node.random else None

            node = node.next
        
        return old2New[head]