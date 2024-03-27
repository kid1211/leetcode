class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        @cache
        def check(pre, post):
            foundPre = foundPost = False
            for l in order:
                if l == pre:
                    if foundPost:
                        print('1', foundPre, foundPost)
                        return False
                    foundPre = True
                elif l == post:
                    if not foundPre:
                        return False
                    foundPost = True
            return foundPre == foundPost == True
        
        for i in range(1, len(words)):
            pre, post = words[i - 1], words[i]
            n = min(len(pre), len(post))
            for j in range(n):
                if pre[j] != post[j]:
                    if check(pre[j], post[j]):
                        break
                    else:
                        return False
                elif j == n - 1 and len(pre) > len(post):
                    return False
        
        return True
