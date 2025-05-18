class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
class Trie:
    def __init__(self, products):
        self.root = TrieNode()

        for product in products:
            self.insert(product)

    def insert(self, word):
        node = self.root
        for l in word:
            if l not in node.children:
                node.children[l] = TrieNode()
            node = node.children[l]
        node.word = word

    def find(self, word):
        node = self.root
        for l in word:
            if l not in node.children:
                return None
            node = node.children[l]
        return node

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie(products)

        @cache
        def dfs(target):
            if not target:
                return []

            # TODO: exit Criteria
            # if len(curr) == 3:
            #     return curr

            node = trie.find(target)

            if not node:
                print("should not be here")
                return []

            if node.word:
                res = [node.word]
            else:
                res = []
    

            for l in "abcdefghijklmnopqrstuvwxyz":
                if l in node.children:
                    res += dfs(target + l)
                    if len(res) >= 3:
                        return res[:3]
            return res
                # dfs()

        
        res = []
        for i in range(1, len(searchWord)+1):
            res += [dfs(searchWord[:i])]
        return res


