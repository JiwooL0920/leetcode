# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# 1. use a lot of built in functions 
class Solution:
    def isPalindrome(self, s):
        newStr = "" 
        for c in s: 
            if c.isalnum(): 
                newStr += c.lower() 
        return newStr == newStr[::-1] #reversed string 
    
# 2. no extra memory 
# left and right pointer 
# use ASCII to determine if a character is alphanumeric 
# numbers: 0-0 (48-57)
# upper case: A-Z (65-90)
# lower case: a-z (97-122)
# Time: O(N)
# Memory: O(1)
class Solution: 
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r: 
            # increment/decrement pointer until characters are alphanumeric 
            while l < r and not self.alphaNum(s[l]): 
                l += 1 
            while r > l and not self.alphaNum(s[r]): 
                r -= 1 
            # check if it's palindrome 
            if s[l].lower() != s[r].lower():
                return False 
            l, r = l + 1, r - 1
        return True 
        
    def alphaNum(self, c):
        # upper case
        return (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))
            









# my own solution
# try 1
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isAlphaNumeric(c):
            return (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))
        
        start = 0 
        end = len(s)-1
        
        while start < end:
            while start < end and not isAlphaNumeric(s[start]):
                start += 1
            while start < end and not isAlphaNumeric(s[end]):
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1 
        
        return True
        
        
