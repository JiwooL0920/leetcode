# Feb 1, 2025
# https://leetcode.com/problems/longest-repeating-character-replacement/description/

# Time: O(26*N)
# Space: O(N)
class Solution:
    def characterReplacement(self, s: str, k:int) -> int:
       count = {}
       res = 0

       l = 0
       for r in range (len(s)):
           # update count
           count[s[r]] = 1 + count.get(s[r], 0)
           # max frequency
           maxf = max(maxf, count[s[r]])
           # if we cant make consecutive characters anymore, shrink left window
           while (r-l+1) - maxf > k:
               count[s[l]] -= 1
               l += 1
            res = max(res, r - l + 1)

