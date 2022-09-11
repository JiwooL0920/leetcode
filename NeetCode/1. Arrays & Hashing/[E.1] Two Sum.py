# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# 1. Brute force
# check every combination that makes the sum 
# Time: O(N^2)

# 2. One pass
# 4 - 1 = 3   need to just check if 3 exists in the array 
# if it doesn't exist in the hashmap, add its val:index in the hashmap 
# hashmap   val:index 
# Time: O(N)
# Mem: O(N)

class Solution:
    def twoSum(self, nums, target):
        prevMap = {} # val : index 
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap: 
                return [prevMap[diff], i]
            prevMap[n] = i 
        return # but we're guaranteed there's a solution 
    

# ========================    
# my own solution 
# [try 1]
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indexMap:
                return [indexMap[diff], i]
            indexMap[n] = i 
            
            
        