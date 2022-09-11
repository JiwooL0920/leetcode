# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: nums = [1,1]
# Output: [2]

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        numSet = set(nums)
        for i in range(1, len(nums)+1):
            if i not in numSet:
                res.append(i)
        return res
   
# neetcode 
# T:O(N), M:O(1)
class Solution:
    def findDisappearedNumbers(self, nums):
        # mark existing
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])
        
        res = []
        for i,n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        
        return res