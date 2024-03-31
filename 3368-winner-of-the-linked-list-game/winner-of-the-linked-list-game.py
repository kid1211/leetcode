# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        score = 0

        while head and head.next:
            score += 1 if head.val > head.next.val else -1
            head = head.next.next
        
        if score > 0:
            return "Even"
        elif score < 0:
            return "Odd"
        else:
            return "Tie"