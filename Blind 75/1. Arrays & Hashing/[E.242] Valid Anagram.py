# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# 1. count the occurrences of each character in both strings using hashmap 
# Time: O(S+T)
# Memory: O(S+T)

class Solution:
    def isAnagram(self, s, t):
        # check if they are same length
        if len(s) != len(t): 
            return False 
        # iterate through each string
        countS, countT = {}, {}
        for i in range(len(s)):
            #                   if this key doesnt exist, default value is 0; avoid key error
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # iterate though each map
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        # they are anagrams 
        return True 
            
            
# O(1) memory? 
# put in sorted order -> become same string 
# time: O(NlogN)
class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t) 