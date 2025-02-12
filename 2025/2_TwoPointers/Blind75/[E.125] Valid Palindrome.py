# 01/25/2025
# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def alphaNum(self, c: str):
        return (
            ord('A') <= ord(c) <= ord('Z')
            or ord('a') <= ord(c) <= ord('z')
            or ord('0') <= ord(c) <= ord('9')
        )

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            # check alphanumeric
            while i < j and not self.alphaNum(s[i]):
                i += 1
            while i < j and not self.alphaNum(s[j]):
                j -= 1
            # check the character
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

# -----------------------------------------------------------------------
# Review: Feb 11, 2025
class Solution:
    def isAlphaNum(self, c: str):
        return (
           ord('a') <= ord(c) <= ord('z')
           or ord('0') <= ord(c) <= ord('9')  
        )

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l <= r:
            cl, cr = s[l].lower(), s[r].lower()
            if not self.isAlphaNum(cl):
                l += 1
            elif not self.isAlphaNum(cr):
                r -= 1
            else:
                if cl != cr:
                    return False
                l += 1
                r -= 1
        return True
        