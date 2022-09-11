# https://leetcode.com/pro11tinct.

# 1. Brute Force 
# Time: O(N^2)
# Space: O(1)

# 2. Sorting 
# Any duplicate will be adjacent (only need to iterate once, check adjacent values) 
# Time: O(NlogN)
# Space: O(1)

# 3. Use HashSet (extra memory)
# Insert and check element in O(1)

class Solution:
    def containsDuplicate(self, nums):
        hashset = set() 
        for n in nums:
            # check if there's a duplicate in hashset
            if n in hashset:
                return True 
            # if not, add it to hashset 
            hashset.add(n)
        return False 