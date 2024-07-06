class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        l2r = True

        while time:
            if n > time:
                break
            time -= (n - 1)
            l2r = not l2r

        return time + 1 if l2r else n - time