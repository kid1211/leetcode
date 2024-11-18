class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
    
        # assume k < len(code)
        n = len(code)

        if k < 0:
            code = code[::-1]
        
        curr = sum(code[:abs(k) + 1])

        
        res = []
        r = abs(k)
        for i in range(n):
            res += [curr - code[i]]
            r = (r + 1) % n
            curr -= code[i]
            curr += code[r]

        

        return res if k > 0 else res[::-1]