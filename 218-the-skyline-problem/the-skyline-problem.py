from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        stack = SortedList()
        res = []

        tmp = []
        for start, end, height in buildings:
            tmp += [(start, end, height)]
            tmp += [(end, end, height)]
        

        for pos, currHeight_end, height in sorted(tmp):
            if pos == currHeight_end: # represent ending
                removeList = []
                for stack_height, height_end in stack:
                    if pos >= height_end:
                        removeList += [(stack_height, height_end)]
                for item in removeList:
                    stack.remove(item)
            else:
                stack += [(height, currHeight_end)]
            # Make sure Stack is correct

            currHeight = stack[-1][0] if stack else 0
            while res and res[-1][0] == pos:
                _, prevHeight = res.pop()
                currHeight = max(currHeight, prevHeight)
    
            if not res or res[-1][1] != currHeight:
                res += [[pos, currHeight]]

        return res
