# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example 2:
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s): return [] 
        
        pCount, sCount = {}, {}
        # compare first substring  
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i],0)
            sCount[s[i]] = 1 + sCount.get(s[i],0)
            
        res = [0] if sCount == pCount else []
        l = 0 
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1 

            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1 
            if sCount == pCount: 
                res.append(l)
                
        return res 
        
        
        
# my solution
from collections import defaultdict 
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        
        mapS, mapP = defaultdict(int), defaultdict(int)
        for i in range(len(p)):
            mapS[s[i]] += 1
            mapP[p[i]] += 1 
        
        res = []
        if mapS == mapP:
            res.append(0)
            
        l = 0
        for r in range (len(p), len(s)):
            mapS[s[r]] += 1 
            mapS[s[l]] -= 1
            if mapS[s[l]] == 0:
                del mapS[s[l]]
            l += 1
            if mapS == mapP:
                res.append(l)
                
        return res
            
                    