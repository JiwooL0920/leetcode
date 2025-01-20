# 22:52 1/19

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
