# 22:52 1/19
# https://leetcode.com/problems/group-anagrams/description/

# Solution 1 - Sorting
# sorting solution = O (M * N log N)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

# Solution 2 - Hashmap
# at most 26 unique characters
# for each string, count the frequency of each character
# hashmap - key = 1e, 1a, 1t (pattern), value = list of strings that match the pattern (ex. eat, tea, ate)

# Time: O(N * M), N = number of strings, M = length of the longest string
# Space: O(N * M)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict to handle case where key doesnt exist
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 # a..z
            for c in s:
                count[ord(c) - ord("a")] +=  1
            # list cant be keys
            res[tuple(count)].append(s)
        return res.values()

# -----------------------------------------------------------------------
# Review: Feb 6, 2025
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      # initalize new keys with empty list
      resmap = defaultdict(list)

      # iterate through string
      for s in strs:
        # create a list of character count, where each index represents the ord representation of the character
        charcount = [0]*26
        # iterate through characters in c
        for c in s:
          # determine ord value of that character
          ordd = ord(c) - ord('a')
          # increment character count
          charcount[ordd] += 1
        # store character count list as key in the result map
        # NOTE: cant have list as key in a python dict -- need to convert into tuple
        resmap[tuple(charcount)].append(s)

      # for final output, turn the groups back from tuple to list
      return [list(group) for group in resmap.values()]
