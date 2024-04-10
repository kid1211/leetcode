class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        
        def dfs(curr, mini, maxi):
            if curr >= len(preorder):
                return curr, True
            # exit?

            root = preorder[curr]
            if not mini <= root <= maxi:
                return curr, False

            leftEnd, left = dfs(curr + 1, mini, root)
            rightEnd, right = dfs(leftEnd, root, maxi)

            return rightEnd, left or right
        
        return dfs(0, -sys.maxsize, sys.maxsize)[1]