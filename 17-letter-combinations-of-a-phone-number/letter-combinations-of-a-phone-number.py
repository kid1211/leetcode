mapping = {
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
        if not digits:
            return []

        def dfs(idx):
            if idx == len(digits) - 1:
                return list(mapping[digits[idx]])

            res = []
            suffixes = dfs(idx + 1)
    
            for suffix in suffixes:
                for l in mapping[digits[idx]]:
                    res += [l + suffix]
            return res

        return dfs(0)
