# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

# O(N)
# hashmap
# prefixSum : count 

class Solution:
    def subarraySum(self, nums, k):
        res = 0 
        curSum = 0 
        prefixSums = { 0:1 }
        
        for n in nums: 
            curSum += n 
            diff = curSum - k 
            res += prefixSums.get(diff,0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        
        return res 