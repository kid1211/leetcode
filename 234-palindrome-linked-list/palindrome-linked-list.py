# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        
        flip = slow.next
        last = slow.next = None

        while flip:
            nxt = flip.next
            flip.next = last
            last = flip
            flip = nxt
        # print(last, head)
        # compare head and flip
        while head and last and head.val == last.val:
            head = head.next
            last = last.next
        
        if head and last:
            return head.val == last.val
        return True

        

        