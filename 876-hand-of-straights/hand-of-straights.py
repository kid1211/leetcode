class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0 or n == 0:
            return False

        hand.sort()
        # keep the actual array, later reduce to a variable
        groups = int(n / groupSize)
        res = [ [] for _ in range(groups) ]
        for num in hand:
            notAdded = True
            for i in range(groups):
                if len(res[i]) == groupSize:
                    continue
                if not res[i] or res[i][-1] == num - 1:
                    res[i] += [num]
                    notAdded = False
                    break
            if notAdded:
                return False


        print(res)
        return True

# 1 2 2 3 3 4 6 7 8