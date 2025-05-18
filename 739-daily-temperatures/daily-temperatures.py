class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [ 0 ] * len(temperatures)
        print(res)

        mono = []

        for i in range(len(temperatures)):
            if not mono or temperatures[i] < temperatures[mono[-1]]:
                mono += [i]
            else:
                while mono and temperatures[i] > temperatures[mono[-1]]:
                    idx = mono.pop()
                    res[idx] = i - idx
                mono += [i]

            #     res += [0]
            # # elif temperatures[i] > temperatures[mono[-1]]:
            #     res += [0]
            #     while mono and temperatures[i] > temperatures[mono[-1]]:
            #         mono.pop()
            #     mono += [i]
            # else:
            #     while mono and temperatures[i] > temperatures[mono[-1]]:
            #         mono.pop()
            #     print(mono)
            #     res += [(mono[-1] - i)]
            #     mono += [i]
        # res.reverse()
        return res
            