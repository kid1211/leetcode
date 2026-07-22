class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:
        n, m = len(s), len(queries)
        cnt1 = s.count("1")

        left = [
            -1
        ] * n  # left[i]: represents the length of the continuous block ending at position i, which is the same as s[i]
        right = [
            -1
        ] * n  # right[i]: represents the length of the continuous block starting at position i with the same value as s[i]
        for i in range(n):
            left[i] = left[i - 1] + 1 if i > 0 and s[i - 1] == s[i] else 1
        for i in range(n - 1, -1, -1):
            right[i] = right[i + 1] + 1 if i < n - 1 and s[i + 1] == s[i] else 1

        ans = [-1] * m
        block_size = isqrt(n)

        longQueries = []  # query with length greater than block length

        def brute_force(l, r) -> int:
            i = l
            best = 0
            prev = -inf

            while i <= r:
                start = i

                while i <= r and s[i] == s[start]:
                    i += 1

                if s[start] == "0":
                    cur = i - start
                    best = prev + cur if prev + cur > best else best
                    prev = cur
            return best

        for i, (l, r) in enumerate(queries):
            if r - l + 1 > block_size:
                longQueries.append((l // block_size, l, r, i))
            else:
                ans[i] = cnt1 + brute_force(
                    l, r
                )  # queries shorter than block length, brute-force calculation

        # sort by the ID of the block where the left endpoint is located as the first keyword, and by the right endpoint as the second keyword
        longQueries.sort(key=lambda q: (q[0], q[2]))
        subZeroBlocks = deque()

        for i, (bid, l, r, qid) in enumerate(longQueries):
            if (
                i == 0 or bid > longQueries[i - 1][0]
            ):  # traverse to a new block, perform initialization operations
                L = (
                    bid + 1
                ) * block_size - 1  # L is initialized as the right endpoint of the block
                R = (
                    bid + 1
                ) * block_size  # R is initialized as the left endpoint of the next block
                subZeroBlocks.clear()
                bestGain = 0

            while R <= r:
                sz = min(r - R + 1, right[R])
                if s[R] == "0":
                    if subZeroBlocks and s[R - 1] == "0":
                        subZeroBlocks[-1] += sz
                    else:
                        subZeroBlocks.append(sz)
                    if len(subZeroBlocks) >= 2:
                        bestGain = max(
                            subZeroBlocks[-1] + subZeroBlocks[-2], bestGain
                        )
                R += sz

            tmp_bestGain = bestGain  # before moving the left endpoint L, backup the value of bestGain
            tmp_firstValue = (
                subZeroBlocks[0] if subZeroBlocks else None
            )  # value of the first element of subZeroBlocks before moving the left endpoint
            cnt = 0  # the number of digits added from the left during the process of recording the movement of the left endpoint L

            while L >= l:
                sz = min(L - l + 1, left[L])
                if s[L] == "0":
                    if subZeroBlocks and s[L + 1] == "0":
                        subZeroBlocks[0] += sz
                    else:
                        subZeroBlocks.appendleft(sz)
                        cnt += 1
                    if len(subZeroBlocks) >= 2:
                        bestGain = max(
                            subZeroBlocks[0] + subZeroBlocks[1], bestGain
                        )
                L -= sz

            ans[qid] = bestGain + cnt1  # answering inquiries

            # restore left endpoint L
            L = (bid + 1) * block_size - 1

            # restore bestGain
            bestGain = tmp_bestGain

            # restore subZeroBlocks
            for _ in range(cnt):
                subZeroBlocks.popleft()
            if tmp_firstValue:
                subZeroBlocks[0] = tmp_firstValue
        return ans