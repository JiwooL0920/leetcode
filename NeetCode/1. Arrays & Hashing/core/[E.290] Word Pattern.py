# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

class Solution:
    def wordPattern(self, pattern, s):
        words = s.split(" ")
        if len(pattern) != len(words):
            return False 

        charToWord = {}
        wordToChar = {} 
        
        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False 
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w 
            wordToChar[w] = c 
        
        return True 