class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        lowest = None
        if len(s) != len(goal):
            return False
        freq = defaultdict(list)

        for i in range(len(s)):
            freq[s[i]] += [i]

            # if not lowest or len(freq[lowest]) > len(freq[s[i]]):
            if not lowest or len(freq[lowest]) > len(freq[s[i]]):
                lowest = s[i]
        
        for goal_i in range(len(goal)):
            if goal[goal_i] != lowest:
                continue
            expect = goal[goal_i:] + goal[:goal_i]
            for idx in freq[lowest]:
                # print(expect, lowest, freq)
                if expect == s[idx:] + s[:idx]:
                    return True
            return False

        return False

            