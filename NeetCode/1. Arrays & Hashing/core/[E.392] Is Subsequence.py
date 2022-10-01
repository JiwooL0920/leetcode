# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.


# My solution
# T: O(N)
# M: O(1)

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # s is empty string
        if not s: return True 
        # s is longer than t
        if len(s) > len(t): return False 
        
        i = 0
        for j in range(len(t)):
            if t[j] == s[i]:
                i += 1 
            # if we went over all char in s
            if i == len(s): 
                return True
                
        return False
                
# Neetcode
class Solution:
    def isSubsequence(self, s, t):
        i, j = 0, 0 
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1 
            j += 1 
            
        return True if i == len(s) else False 