class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def getPrefix(length):
            res = ""

            for i in range(length):
                matched = None
                for word in strs:
                    if i >= len(word):
                        return res

                    if matched is None:
                        matched = word[i]
                    elif matched != word[i]:
                        return res
                res += matched
            return res

        left, right = 0, 201

        while left + 1 < right:
            mid = (left + right) // 2

            if getPrefix(mid) == "":
                right = mid
            else:
                left = mid

        res = getPrefix(right)
        if res != "":
            return res
        else:
            return getPrefix(left)
