# Given a list of integers nums sorted in ascending order and an integer k, return whether any two elements from the list add up to k. You may not use the same element twice.

# Note: Numbers can be negative or 0.

# This should be done in \mathcal{O}(1)O(1) space.

# Input
# nums = [1, 3, 5, 8]
# k = 6
# Output
# True


class Solution:
    def solve(self, nums, k):
        if len(nums) < 2: return False
        l, r = 0, len(nums)-1
        while l < r:
            s = nums[l] + nums[r]
            # print(s)
            if s < k:
                l += 1
            elif s > k:
                r -= 1
            else:
                return True
        return False