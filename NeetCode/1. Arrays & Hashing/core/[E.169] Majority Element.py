# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# T: O(N)
# M: O(N)
class Solution:
    def majorityElement(self, nums):
        count = {}
        res, maxCount = 0, 0 
        
        for n in nums: 
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res 
            maxCount = max(count[n], maxCount)
        
        return res 
            
# Boyer-Moore (w/o hashmap)
# T: O(N)
# M: O(1)
class Solution:
    def majorityElement(self, nums):
        res, count = 0, 0 
        for n in nums:
            if count == 0:
                res = n 
            count += (1 if n == res else -1)