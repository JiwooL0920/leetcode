# Given a string s, find two disjoint palindromic subsequences of s such that the product of their lengths is maximized. The two subsequences are disjoint if they do not both pick a character at the same index.

# Return the maximum possible product of the lengths of the two palindromic subsequences.

# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters. A string is palindromic if it reads the same forward and backward.

#  Input: s = "leetcodecom"
# Output: 9
# Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
# The product of their lengths is: 3 * 3 = 9.
# Example 2:

# Input: s = "bb"
# Output: 1
# Explanation: An optimal solution is to choose "b" (the first character) for the 1st subsequence and "b" (the second character) for the 2nd subsequence.
# The product of their lengths is: 1 * 1 = 1.
# Example 3:

# Input: s = "accbcaxxcxx"
# Output: 25
# Explanation: An optimal solution is to choose "accca" for the 1st subsequence and "xxcxx" for the 2nd subsequence.
# The product of their lengths is: 5 * 5 = 25.

#   e   t       e
# l e e t c o d e c o m 
#         c   d   c 


# bitmask --> "disjoint" subsequence
# leetcodecom
# 00000000000  (11 zeroes)
# 1 at every spot we found character
# 01010001000 (ete)
# 00001010100 (cdc) 
# ----------------- &
# 00000000000 all zero --> disjoint 
 
# for i = 1 --> 2^11 (not including 11)
# how to convert binary representation to check if subsequence is palindrome?
# add to output -> ete. reverse it and check if equal 

# maintain hashmap[key=bitmask (binary representation of string): value=length of palindrome]

# T: O(4^n)
# M: O(N)

class Solution:
    def maxProduct(self, s):
        N, pali = len(s), {} # bitmask : length 
        for mask in range(1, 1 << N): # 1 << N = 2 ** N
            subseq = ""
            for i in range(N):
                if mask & (1 << i): # index in string s
                    subseq += s[N - i - 1] # s[i] works 
                if subseq == subseq[::-1]:
                    pali[mask] = len(subseq)
        
        
        for m1 in pali:
            for m2 in pali: 
                if m1 & m2 == 0: # disjoint 
                    res = max(res, pali[m1] * pali[m2])
                    
        return res 
