# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []

# 1) for all num, convert to index and - the num at the index (flag it)
# 2) if there's a duplicate, n at index will already be - 

class Solution(object):
    def findDuplicates(self, nums):
        ans = []
        for num in nums:
            i = abs(num)-1
            if nums[i] < 0:
                ans.append(abs(num))
            else:
                nums[i] *= -1
        return ans