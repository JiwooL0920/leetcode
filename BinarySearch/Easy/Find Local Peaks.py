# You are given a list of integers nums. Return the index of every peak in the list, sorted in ascending order. An index i is called a peak if:

# nums[i] > nums[i + 1] if i = 0
# nums[i] > nums[i - 1] if i = n - 1
# nums[i - 1] < nums[i] > nums[i + 1] otherwise
# However, a list of length 1 is not considered a peak.

# Constraints

# 0 ≤ n ≤ 100,000 where n is the length of nums

# Input
# nums = [1, 2, 3, 2, 4]
# Output
# [2, 4]

# Time: O(N)
# Mem: O(1)

class Solution:
    def solve(self, nums):
        res = []

        # empty of single nums
        if len(nums) < 2:
            return res 

        # start
        if nums[0] > nums[1]: 
            res.append(0)
        # end
        if nums[-1] > nums[-2]:
            res.append(len(nums)-1)

        # compare left, i, right
        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                res.append(i)
        
        res.sort()
        return res