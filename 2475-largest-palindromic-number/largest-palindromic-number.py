class Solution:
    def largestPalindromic(self, num: str) -> str:
        largest_Odd = None
        counter = [0] * 10

        for l in num:
            counter[int(l)] += 1

        half = ""
        for i in range(9, -1, -1):
            if counter[i] == 0:
                continue
            if counter[i] % 2 == 1 and not largest_Odd:
                largest_Odd = i

            if not half and i == 0:
                continue
            half += str(i) * (counter[i] // 2)
        
        if largest_Odd is not None:
            return half + str(largest_Odd) + half[::-1]
        elif half:
            return half + half[::-1]
        else:
            return "" if counter[0] == 0 else "0"