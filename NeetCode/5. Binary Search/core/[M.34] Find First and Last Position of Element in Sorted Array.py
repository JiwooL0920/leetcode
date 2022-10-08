# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]


# my solution
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums)-1 
        
        while l <= r:
            m = (l+r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1 
            else:
                start, end = m, m
                while start >= 0 and nums[start] == target:
                    start -= 1
                while end < len(nums) and nums[end] == target:
                    end += 1 
                return [start+1, end-1]
        
        return [-1, -1]
                
                
# neetcode
class Solution:
    def searchRange(self, nums, target):
     left = self.binSearch(nums, target, True)
     right = self.binSearch(nums, target, False)
     return [left, right]
     # leftBias = [True/False], if flase, res is rightBiased   
    def binSearch(self, nums, target, leftBias):                
        l, r = 0, len(nums)-1
        i = -1
        while l <= r:
            m = (l+r) // 2
            if target > nums[m]:
                l = m + 1 
            elif target < nums[m]:
                r = m - 1 
            else: 
                i = m 
                if leftBias: 
                    r = m - 1 
                else: 
                    l = m + 1
        return i 
                