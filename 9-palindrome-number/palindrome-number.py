class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        tmp = str(x)
        left, right = 0, len(tmp) - 1
        while left < right:
            if tmp[left] != tmp[right]:
                return False
            left += 1
            right -= 1
        
        return True