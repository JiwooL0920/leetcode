# Feb 1, 2025
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Time: O(N)
# Space: O(N)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        res = 0
        l = 0
        for r in range(len(s)):
            # shrink left window until there is no duplicate
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            # expand right window while no duplicate is found
            res = max(res, r-l+1)
            unique.add(s[r])
        return res


