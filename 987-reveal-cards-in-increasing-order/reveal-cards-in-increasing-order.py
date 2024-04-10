class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # [2, 3, 5, 7, 11, 13, 17]
        # 2,13,3,11,5,17,7
        
        # [13, 17] # 13 -> [17]
        # [11, 17, 13] # 11 -> [13, 17]
        # [7, 13, 11, 17]. # 7 -> [11, 17, 13]
        # # move last up
        # [5, 17, 7, 13, 11]
        # [3, 11, 5, 17, 7, 13]
        # [2, 13, 3, 11, 5, 17, 7]
        deck.sort(reverse=True)
        res = deque()
        for num in deck:
            # if not res:
            #     res += [num]
            # elif len(res) == 1:
            #     res.appendleft(num)
            # else:
            #     right = res.pop()
            #     res.appendleft(right)
            #     res.appendleft(num)
            if len(res) > 1:
                res.appendleft(res.pop())
            res.appendleft(num)
        
        return list(res)