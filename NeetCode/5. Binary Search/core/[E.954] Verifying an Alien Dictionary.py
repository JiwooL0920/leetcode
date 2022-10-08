# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

# O(c)

class Solution:
    def isAlienSorted(self, words, order):
        orderInd = { c:i for i,c in enumerate(order) }
        
        for i in range(len(words) - 1):
            # compare 2 words
            # w1 is lexicographically smaller than w2 
            w1, w2 = words[i], words[i+1] 
            
            # compare every cahracter in w1 and w2 
            for j in range(len(w1)):
                # prefix out of order (len(w1) <= len(w2))
                if j == len(w2):
                    return False 

                # found differing character
                if w1[j] != w2[j]:
                    # char at w1 is lexicographically greater than char at w2 --> invalid
                    if orderInd[w2[j]] < orderInd[w1[j]]:
                        return False 
                    # in lexi order. we don't have to compare thru rest of char 
                    break 
        
        return True 
            