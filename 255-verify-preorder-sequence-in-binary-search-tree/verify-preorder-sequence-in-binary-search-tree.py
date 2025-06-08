class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        
        def dfs(curr, mini, maxi):
            if curr >= len(preorder):
                return curr, True
            # exit?

            rootVal = preorder[curr]
            if not mini <= rootVal <= maxi:
                return curr, False

            leftEnd, left = dfs(curr + 1, mini, rootVal)
            rightEnd, right = dfs(leftEnd, rootVal, maxi)

            return rightEnd, left or right
        
        return dfs(0, -sys.maxsize, sys.maxsize)[1]