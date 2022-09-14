# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# 1. take each one of the strings and sort them 
# Time: O(m x NlogN)   

# 2. better 
# hashmap: 
#     a-z (26)    at most 26 elements 
#     1e, 1a, 1t  :   [eat, tea, ate]
# Time: O(m x n)  m = total number of elements, n = avg num of characters in each string 
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs): 
        #  defaultdict never raises a KeyError. It provides a default value for the key that does not exists.
        res = defaultdict(list) # mapping charCount to list of Anagrams 
        for s in strs: 
            count  = [0] * 26 # a...z
            for c in s: 
                count[ord(c) - ord("a")] += 1
                # a = 80 -> 0 (80-80)
                # b = 81 -> 1 (81-80)
            # in python, lists cannot be keys so tuple 
            res[tuple(count)].append(s) 
        return res.values()

# print(res)
# defaultdict(<class 'list'>, {(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat', 'tea', 'ate'], (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['tan', 'nat'], (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['bat']})

n = Solution() 
n.groupAnagrams(["eat","tea","tan","ate","nat","bat"])




# ========================    
# my own solution 
# [try 1]
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # [e:1, a:1, t:1] : ["eat","tea","ate"] --> doesn't work. dict/list cannot be a dict key 
        
        # use ord.
        # a = 80 -> 0 (80-80)
        # b = 81 -> 1 (81-80)
        
        res = {}
        
        for s in strs:
            chars = [0]*26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            a = res.get(tuple(chars),[])
            a.append(s)
            res[tuple(chars)] = a
        
        return res.values()
                
                