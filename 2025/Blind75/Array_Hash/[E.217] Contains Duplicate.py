# Date: 01/17/2025

# https://leetcode.com/problems/contains-duplicate/description/

# Brute Force
# Time, Space: O(N)
# Hashmap insert and search: O(1) 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for n in nums:
            if n in hashmap.keys():
                return True
            hashmap[n] = 1
        return False

# If sorting:
# Time: O(NlogN), Space: O(1)
# Slightly better than brute force

# Neetcode solution
# Hashset
# Time, Space: O(N)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False