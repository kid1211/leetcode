from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        stack = SortedList()
        res = []

        tmp = []
        for start, end, height in buildings:
            tmp += [(start, end, height, False)]
            tmp += [(end, end, height, True)]
        

        for pos, currHeight_end, height, isEnd in sorted(tmp):
            if isEnd:
                stack = SortedList([item for item in stack if pos < item[1]])
                # removeList = []
                # newStack = 
                # for stack_height, height_end in stack:
                #     if pos >= height_end:
                #         removeList += [(stack_height, height_end)]
                # for item in removeList:
                #     stack.remove(item)
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
