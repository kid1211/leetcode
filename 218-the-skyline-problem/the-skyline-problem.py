from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        stack = SortedList()
        res = []

        tmp = []
        for start, end, height in buildings:
            tmp += [(start, end, height, False)]
            tmp += [(end, end, height, True)]
        

        for pos, key, height, isEnd in sorted(tmp):
            if isEnd:
                removeList = []
                for stack_height, stack_key in stack:
                    if pos >= stack_key:
                        removeList += [(stack_height, stack_key)]
                for item in removeList:
                    stack.remove(item)
            else:
                stack += [(height, key)]
            # Make sure Stack is correct

            currHeight = stack[-1][0] if stack else 0
            while res and res[-1][0] == pos:
                _, prevHeight = res.pop()
                currHeight = max(currHeight, prevHeight)
    
            if not res or res[-1][1] != currHeight:
                res += [[pos, currHeight]]

        return res
