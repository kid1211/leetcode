# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        last = None
        while fast and fast.next:
            last = slow
            slow = slow.next
            fast = fast.next.next
        
        # print(slow.val, last.val)
        if not last:
            return None
        last.next = last.next.next
        return head