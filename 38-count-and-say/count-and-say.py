class Solution:
    def countAndSay(self, n: int) -> str:
        
        def read(text):
            last = None
            count = 0
            res = ""
            for digit in text:
                if not last or digit == last:
                    count += 1
                else:
                    res += str(count) + str(last)
                    count = 1

                last = digit
            if count > 0:
                res += str(count) + str(last)

            return res
        
        def dfs(idx):
            if idx == n - 1:
                return "1"
            return read(dfs(idx + 1))

        return dfs(0)