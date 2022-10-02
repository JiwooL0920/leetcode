# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

# Example 1:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:

# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]

class Solution:
    def findRepeatedDnaSequences(self, s): 
        seen,res = set(), set() 
        
        # at least 9 characters come after so we have a window of 10 characters including l 
        for l in range(len(s) - 9):
            cur = s[l:l+10]
            if cur in seen:
                res.add(cur)
            else:
                seen.add(cur)
        return res