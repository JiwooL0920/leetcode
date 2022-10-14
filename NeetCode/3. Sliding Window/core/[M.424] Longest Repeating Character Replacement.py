# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Brute force O(N^2)

# Better solution using sliding window 
# Time: O(N)
# we want all characters in a particular window to match the most common character in that window 
# hashmap/array that takes every single character and count the number of occurences of each character

# A|BABB|A
# A:1
# B:3 
# windowLen - count[B] <= k 
# 4 - 3 = 1 <= k  -->  number of characters in our window that we need to replace to match the most frequent character 
# as long as this condition is true, our current window is valid 
# we have enough replacements to make in our current window 
# how to know which character is most frequent? --> use hashmap O(N)
# add sliding window technique. start from left, expand as much as we can to the right. if condition fails, shift left pointer and repeat 
# when shifting left pointer, we need to update our hashmap (derement)
# but use algorithm to avoid looking thru hashmap to find most frequent char
# --> maxf variable. 
# length - maxf <= k 
# leaving maxf when left pointer increments doesnt change the result 

class Solution: 
    def characterReplacement(self, s, k):
        count = {}
        res = 0
        l = 0
        maxf=0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # element at right pointer
            maxf = max(maxf, count[s[r]]) 
            #check if current window is valid 
            # while (r-l+1) - max(count.values()) > k:
            while (r-l+1) - maxf > k:
                count[s[l]] -= 1 
                l += 1 
            res = max(res, r-l+1) #size of window 
        return res 
    
    
# my own solution
from collections import defaultdict 
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l, r = 0, 0
        freq = defaultdict(int)
        mostFreq = 0
        res = 0
        
        for r in range(len(s)):
            freq[s[r]] += 1 
            mostFreq = max(mostFreq, freq[s[r]])
            while (r-l+1) - mostFreq > k:
                freq[s[l]] -= 1
                l += 1 
            res = max(res, r-l+1)
            
        return res
            
                