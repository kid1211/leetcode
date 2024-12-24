class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:


        def build_tree(edges):
            res = defaultdict(list)
            for a, b in edges:
                res[a] += [b]
                res[b] += [a]
            return res

        def dfs(node, tree, parent):
            maxDiameter = longest = secondlongest = 0

            for nxt in tree[node]:
                if nxt == parent:
                    continue
                diameter, length = dfs(nxt, tree, node)
                maxDiameter = max(maxDiameter, diameter)
                if length > longest:
                    longest, secondlongest = length, longest
                elif length > secondlongest:
                    secondlongest = length

            return max(
                maxDiameter,
                longest + secondlongest
            ), longest + 1

        tree1, tree2 = build_tree(edges1), build_tree(edges2)
        diameter1, _ = dfs(0, tree1, -1)
        diameter2, _ = dfs(0, tree2, -1)
        print(diameter1, diameter1)
        return max(
            diameter1, diameter2, int(
                math.ceil(diameter1 / 2) +
                math.ceil(diameter2 / 2) + 1)
        )

