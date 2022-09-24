# Given a list of integers sorted in ascending order nums, square the elements and give the output in sorted order.

class Solution:
    def solve(self, nums):
        res = [0] * len(nums)
        i = len(nums)-1

        l, r = 0, len(nums)-1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[i] = nums[l] ** 2
                l += 1
            else:
                res[i] = nums[r] ** 2
                r -= 1
            i -= 1
        return res