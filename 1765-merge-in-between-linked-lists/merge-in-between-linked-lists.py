# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        last = None
        i = 0
        curr = ListNode(next=list1)
        lastA = lastB = None
        while curr:
            curr = curr.next
            last = curr
            i += 1

            if i == a:
                lastA = last
            elif i == b + 1:
                lastB = last
        
        lastA.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = lastB.next
        return list1
