from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heightStack = SortedList()
        endStack = SortedList()
        res = []

        tmp = []
        for start, end, height in buildings:
            tmp += [(start, end, height, False)]
            tmp += [(end, end, height, True)]
        

        for pos, currHeight_end, height, isEnd in sorted(tmp):
            if isEnd:
                # removeList = []
                # for heightStack_height, height_end in heightStack:
                #     if pos >= height_end:
                #         removeList += [(heightStack_height, height_end)]
                # for item in removeList:
                #     heightStack.remove(item)
                while endStack and pos >= -endStack[-1][0]:
                    neg_end, pos_height = endStack.pop()
                    heightStack.remove((pos_height, - neg_end))
            else:
                heightStack += [(height, currHeight_end)]
                endStack += [(-currHeight_end, height, )]
            # Make sure heightStack is correct

            currHeight = heightStack[-1][0] if heightStack else 0
            while res and res[-1][0] == pos:
                _, prevHeight = res.pop()
                currHeight = max(currHeight, prevHeight)
    
            if not res or res[-1][1] != currHeight:
                res += [[pos, currHeight]]

        return res
