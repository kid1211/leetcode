class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        unique1 = defaultdict(set)
        for i in range(len(s)):
            unique1[s[i]].add(i)
        unique2 = defaultdict(set)
        for i in range(len(s)):
            unique2[t[i]].add(i)

        unique1 = sorted(unique1.values())
        unique2 = sorted(unique2.values())
        return unique1 == unique2
        # unique1 = defaultdict(list)
        # unique2 = defaultdict(list)

        # for i in range(len(s)):
        #     unique1[s[i]] += [i]
        # for i in range(len(t)):
        #     unique2[t[i]] += [i]
        # print(unique1.values(), unique2.values())
        # return unique1.values() == unique2.values()
