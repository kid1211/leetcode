class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left, right):
            while left < right and s[left] == s[right]:
                left += 1
                right -= 1
            
            return left, right
        
        initLeft, initRight = isPalindrome(0, len(s) - 1)

        if initLeft >= initRight:
            return True
        
        tmpLeft, tmpRight = isPalindrome(initLeft + 1, initRight)

        if tmpLeft >= tmpRight:
            return True
        
        tmpLeft, tmpRight = isPalindrome(initLeft, initRight - 1)

        if tmpLeft >= tmpRight:
            return True
        
        return False