# Given a list of strings words, group all anagrams together and return the size of the largest grouping.

# Input
# words = ["ab", "ba", "abc", "cba", "bca", "ddddd"]
# Output
# 3

from collections import defaultdict

class Solution:
    def solve(self, words):
        res = defaultdict(int)
        for s in words:
            occ = [0] * 26
            for c in s:
                occ[ord(c) - ord('a')] += 1
            res[tuple(occ)] += 1
        
        maxOcc = 0
        for n in res.values():
            maxOcc = max(n, maxOcc)
        
        return maxOcc