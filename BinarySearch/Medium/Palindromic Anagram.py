# Given a string s, determine whether any anagram of s is a palindrome.

# Input
# s = "carrace"
# Output
# True

from collections import defaultdict 

class Solution:
    def solve(self, s):
        mymap = defaultdict(int)
        for c in s:
            mymap[c] += 1
        odd = 0
        for v in mymap.values():
            if v % 2 != 0:
                odd += 1 
            if odd > 1:
                return False
        return True