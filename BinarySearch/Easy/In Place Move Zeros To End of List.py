# Given a list of integers nums, put all the zeros to the back of the list by modifying the list in-place. The relative ordering of other elements should stay the same.

# Can you do it in \mathcal{O}(1)O(1) additional space?

# Constraints
# 0 ≤ n ≤ 100,000 where n is the length of nums

# Input
# nums = [0, 1, 0, 2, 3]
# Output
# [1, 2, 3, 0, 0]

# T: O(N)

class Solution:
    def solve(self, nums):
        i = 0
        j = 1
        while j <= len(nums)-1:
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[i] == 0 and nums[j] == 0:
                j += 1
            else:
                i += 1
                j += 1
        return nums
