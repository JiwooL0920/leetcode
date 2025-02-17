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


# -------------------------------------------------------------------------------
# Review: Feb 16, 2025
# Time: O(N)
# Space: O(1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        seen = set()
        i = 0
        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            result = max(result, j-i+1)
        return result

