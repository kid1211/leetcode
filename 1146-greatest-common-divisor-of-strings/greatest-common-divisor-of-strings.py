class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1, str2 = (str1, str2) if len(str1) >= len(str2) else (str2, str1)

        # chunk_size = len(str2)

        def check_match(long, short):
            if len(long) % len(short) != 0:
                return False
            chunk = len(short)
            for i in range(len(long) // chunk):
                curr = long[i * chunk:i * chunk + chunk]
                # print((i, len(long) // chunk), (curr, short))
                if curr != short:
                    return False
            return True
        # print((check_match("ABABAB", "AB")))

        # def find_next_size(word):
            # curr = len(word)
            print(curr % 2 != 0, curr == 0)
            # if curr % 2 != 0 or curr == 0:
            #     return ""
            # next_size = curr // 2

            # # USING GLOBAL HERE
            # print(word, str2[:next_size])
            # if (check_match(str2, str2[:next_size])):
            #     return word[:next_size]
            # else:
            #     print("huh")
            #     return find_next_size(str2[:next_size // 2])
        def find_next_size(word):
            if not word:
                return ""
            
            for i in range(len(word) - 2, 0, -1):
                if check_match(str2, str2[:i]):
                    return str2[:i]
            return ""

        # print(check_match("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXX"))
        # print(check_match("TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXX"))
        # print(str2)
        # print(find_next_size(str2))

        res = str2
        while res:
            if check_match(str1, res):
                return res
            else:
                res = find_next_size(res)
        return ""
        # while res:
        #     res = find_next_size(len(res))
#         res = str2
#         while res:
#             if check_match(str1, res):
#                 return res
            
#             # not matching, find next
             
#             for i in range(len(res) - 1, -1, -1):
#                 str2[]
#                 # if check_match(str2, str2[])

#         return ""
# #         return check_match(str1, str2)
