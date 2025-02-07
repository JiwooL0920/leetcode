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


# ---------------------------------------------------
# Review: Feb 6, 2025
# Time: O(N), Space: O(N)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      mapp = {}

      # initialize hashtable with characters in s
      for cs in s:
        mapp[cs] = mapp.get(cs, 0) + 1

      # iterate through characters in t
      for ct in t:
        # if character in t is not in s, its not an anagram
        if ct not in mapp:
          return False
        # decrement character count in map by 1
        mapp[ct] = mapp[ct] - 1
        # if character count goes below 0, it means that t has more character ct than in s, so its not an anagram
        if mapp[ct] < 0:
          return False

      # validate that the sum of character count is exactly 0
      # could be more than 0, meaning s has more character count than t, in which case it is not an anagram
      return sum(mapp.values()) == 0
