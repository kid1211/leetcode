# Fix remove if last and if not head
# directly access next, instead of poping it out in the while loop
class Node:
    def __init__(self, letter, count):
        self.letter = letter
        self.count = count
        self.next = None
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = Counter(s)
        last = None
        head = None
        for l in reversed("abcdefghijklmnopqrstuvwxyz"):
            if l not in counter:
                continue
            curr = Node(l, counter[l])

            if last:
                last.next = curr
            if not head:
                head = curr
            last = curr
        
        res = ""
        last = None
        while head:
            if last:
                lastL, lastC = last
                res += lastL * min(lastC, repeatLimit)
                
                if lastC > repeatLimit:
                    last = (lastL, lastC - repeatLimit)
                else:
                    # might not be needed
                    last = None
                
            if last:
                res += head.letter
                head.count -= 1
                if head.count <= 0:
                    head = head.next
            else:
                last = (head.letter, head.count)
                head = head.next
        
        if last:
            lastL, lastC = last
            res += lastL * min(lastC, repeatLimit)
            
            if lastC > repeatLimit:
                last = (lastL, lastC - repeatLimit)
            else:
                # might not be needed
                last = None
        return res

