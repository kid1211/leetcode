class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = { int(digits[i]): i for i in range(len(digits)) }

        for i in range(len(digits)):
            for digit in range(9, int(digits[i]), -1):
                idx = last.get(digit, -1)

                if idx > i:
                    digits[i], digits[idx] = digits[idx], digits[i]
                    return int("".join(digits))
        return num