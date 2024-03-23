# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        fast = slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        # slow的下一个node开始需要被reverse
        reverse = slow.next
        slow.next = None

        # reverse list
        last = None
        while reverse:
            nxtReverse = reverse.next
            reverse.next = last
            last = reverse
            reverse = nxtReverse
        
        # merge two sorted list
        reverse = last
        forward = head
        dummy = curr = ListNode()
        while reverse and forward:
            curr.next = forward
            nxtFroward = forward.next
            curr.next.next = reverse
            
            curr = reverse
            forward = nxtFroward
            reverse = reverse.next
        
        # only possible to have forward and not reverse
        if forward:
            curr.next = forward

        # Not possible to have reverse
        if reverse:
            return None

        return dummy.next
