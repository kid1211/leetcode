from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        stack = SortedList()
        res = []

        tmp = []
        for start, end, height in buildings:
            tmp += [(start, (start, end), height, False)]
            tmp += [(end, (start, end), height, True)]
        

        for pos, key, height, isEnd in sorted(tmp):
            if isEnd:
                shouldContinue = True
                while stack and shouldContinue:
                    for stack_height, stack_key in stack:
                        if pos >= stack_key[1]:
                            stack.remove((stack_height, stack_key))
                            break
                    shouldContinue = False
            else:
                stack += [(height, key)]
            # print(pos, key, isEnd, stack)
            currHeight = stack[-1][0] if stack else 0
            # [[0,3],[2,0],[2,3],[5,0]]
            # [[0,3],[5,0]]

            # [[1,1],[1,2],[1,3],[2,2],[2,0]]
            # [[1,3],[2,0]]

            # [[1,219],[2,228],[19,225],[45,229],[89,190],[95,175],[97,152],[99,145],[99,74],[100,0]]
            # [[1,219],[2,228],[19,225],[45,229],[89,190],[95,175],[97,152],[99,74],[100,0]]
            
        
            while res and res[-1][0] == pos:
                _, prevHeight = res.pop()
    
                if not currHeight:
                    currHeight = max(currHeight, prevHeight)

            # if not stack and isEnd:
            #     currHeight = 0
    
            res += [[pos, currHeight]]
            
            while res and res[-1][1] == currHeight:
                prevPos, _ = res.pop()
                pos = min(prevPos, pos)

            res += [[pos, currHeight]]

        return res

[[0,3,3],[1,5,3],[2,4,3],[3,7,3]]