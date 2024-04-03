maps = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def dfs(i):
            if i == len(digits) - 1:
                return list(maps[digits[i]])
            if i >= len(digits):
                return []
            res = []
            for l in maps[digits[i]]:
                for tmp in dfs(i + 1):
                    res += [
                        l + tmp
                    ]
            return res
        
        return dfs(0)