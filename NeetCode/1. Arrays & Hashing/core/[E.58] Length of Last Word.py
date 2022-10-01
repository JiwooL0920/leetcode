# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.


# my solution
# T: O(N)
# M: O(1)
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0 
        
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            j = i+1
            while j < len(s) and s[j] != " ":
                j += 1 
            res = len(s[i:j])
            i = j
        
        return res
    

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # eliminate leading empty string
        i = len(s)-1
        while i >= 0 and s[i] == " ":
            i -= 1 
            
        # find end of string 
        j = i-1
        while j >= 0 and s[j] != " ":
            j -= 1
        
        # this is the last word
        return len(s[j+1:i+1])
        
            
# neetcode
# start from the end 
class Solution:
    def lengthOfLastWord(self, s):
        i, length = len(s)-1, 0
        
        while s[i] == " ":
            i -= 1 
        while i >= 0 and s[i] != " ":
            length += 1 
            i -= 1 
        return length