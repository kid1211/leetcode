class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        move = 0

        for direction, amount in shift:
            move += (
                1 if direction == 0 else -1
            ) * amount
        move %= len(s)
        return s[move:] + s[:move]