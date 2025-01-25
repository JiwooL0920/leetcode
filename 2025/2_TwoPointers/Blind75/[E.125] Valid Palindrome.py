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

