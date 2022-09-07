# Given a string s, find the length of the longest substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# previous solution I had 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = ""
        size = len(s)
        substring = "" 
        i = 0
        while i < size: 
            if s[i] in substring:
                if len(substring) > len(result):
                    result = substring 
                substring = "" 
            else:
                substring += s[i]
                i += 1 
        if len(substring) > len(result):
            result = substring 
        return len(result)
        
# Neetcode 
# set only contains 1 character -> use for substring 
# keep move r, if r hits duplicate, remove l (from the window and from the set )
# Time: O(N)
class Solution:
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)): 
            # duplicate -> update window and set
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res 
