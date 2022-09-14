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
    
    
    
    
# ========================    
# my own solution 
# [try 1]
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False 
        
        hashMapS, hashMapT = {}, {} 
        
        for c in s:
            hashMapS[c] = 1 + hashMapS.get(c, 0)
        for c in t:
            hashMapT[c] = 1 + hashMapT.get(c, 0)
            
        for c in hashMapS:
            if c not in hashMapT: return False
            if hashMapS[c] != hashMapT[c]: return False 
            
        return True

