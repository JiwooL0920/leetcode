# Input
# nums = [5, 4, 1, 3, -2, -2]
# Output
# 60

class Solution:
    def solve(self, nums):
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
