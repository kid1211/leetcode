class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()

        left, right = 0, len(tokens) - 1

        while left < right:
            if tokens[left] <= power:
                score += 1
                power -= tokens[left]
                left += 1
            elif score > 0:
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                break

        if left == right and tokens[left] <= power:
            score += 1
            power -= tokens[left]

        return score




# [100,200,300,400], power = 200
# -100
# 100, + 1
# +400
# 500 - 1
# -200
# 300 + 1
# -300
# +2
