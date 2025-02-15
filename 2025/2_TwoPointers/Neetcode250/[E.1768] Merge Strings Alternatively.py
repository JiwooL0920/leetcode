# Feb 15, 2025
# http://leetcode.com/problems/merge-strings-alternately/description/

# Time: O(N)
# Space: O(1)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0
        len1, len2 = len(word1), len(word2)
        while i < len1 or i < len2:
            if i < len1:
                result += word1[i]
            if i < len2:
                result += word2[i]
            i += 1
        return result

