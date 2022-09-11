# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

# Example 1
# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.

# Example 2:
# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.

# Example 3:
# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxList = [float("-inf")] * 3
        for n in nums:
            if n not in maxList:
                if n > maxList[0]:
                    maxList[2] = maxList[1]
                    maxList[1] = maxList[0]
                    maxList[0] = n
                elif n > maxList[1]:
                    maxList[2] = maxList[1]
                    maxList[1] = n 
                elif n > maxList[2]:
                    maxList[2] = n 
            
        if maxList[-1] > float("-inf"):
            return maxList[-1]
        else:
            return maxList[0]