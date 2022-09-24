# You are given a list of integers nums which contains at least one 1. Return whether all the 1s appear consecutively.

# Input
# nums = [0, 1, 1, 1, 2, 3]
# Output
# True

class Solution:
    def solve(self, nums):
        start, end = 0, 0 
        for i in range(len(nums)):
            # found starting point of 1
            if nums[i] == 1:
                end = i
                while end < len(nums) and nums[end] == 1:
                    end += 1
                break
        # find if there's any 1 from the end of consecutive streak 
        for i in range(end, len(nums)):
            if nums[i] == 1:
                return False
        return True