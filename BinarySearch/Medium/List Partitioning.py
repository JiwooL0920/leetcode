# Given a list of strings strs, containing the strings "red", "green" and "blue", partition the list so that the red come before green, which come before blue.

# This should be done in \mathcal{O}(n)O(n) time.

# Bonus: Can you do it in \mathcal{O}(1)O(1) space? That is, can you do it by only rearranging the list (i.e. without creating any new strings)?

# Input
# strs = ["green", "blue", "red", "red"]
# Output
# ["red", "red", "green", "blue"]

# my solution 
class Solution:
    def solve(self, strs):
        start = 0 
        colors = ["red", "green", "blue"]
        for c in range(2):
            for i in range(len(strs)):
                if strs[i] == colors[c]:
                    strs[start], strs[i] = strs[i], strs[start]
                    start += 1 

        return strs
    
    
# dutch flag algorithm
class Solution:
    def solve(self, s):
        def partition(s, start, word):
            for i in range(start, len(s)):
                if s[i] == word:
                    s[i], s[start] = s[start], s[i]
                    start += 1
            return start

        start = partition(s, 0, "red")
        partition(s, start, "green")
        return s
