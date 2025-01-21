# 01/17/2025
# https://leetcode.com/problems/valid-anagram/description/
# Time: O(N), Space: O(N)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if two words are not of same length, its not an anagram
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            cS, cT = s[i], t[i]
            countS[cS] = 1 + countS.get(s[i], 0)
            countT[cT] = 1 + countT.get(t[i], 0)

        return countS == countT
