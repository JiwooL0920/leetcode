# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true
 
# T: O(N)
# M: O(N)
from collections import defaultdict 

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapS, mapT = defaultdict(int), defaultdict(int)
        
        for c in s:
            mapS[c] += 1
        for c in t:
            mapT[c] += 1 
            
        if mapS.values() == mapT.values():
            return True 
    
        return False
        