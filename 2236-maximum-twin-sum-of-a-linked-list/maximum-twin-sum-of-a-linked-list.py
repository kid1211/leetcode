# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = ListNode()
        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode
        
        res = - sys.maxsize
        while head and prev:
            res = max(res, head.val + prev.val)
            head = head.next
            prev = prev.next
        return res