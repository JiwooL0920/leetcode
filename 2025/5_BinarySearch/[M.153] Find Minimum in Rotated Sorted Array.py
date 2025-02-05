# Feb 4, 2025
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# Time: O(log n)
# Space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] # arbitrary, initialized to leftmost value to begin with
        l, r = 0, len(nums)-1

        while l <= r:
            # subarray is sorted in increasing order
            if nums[l] < nums[r]:
                # in which case we return the left most (min) value
                res = min(res, nums[l])
                break
            # apply binary search algorithm
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                # search to the left
                l = m + 1
            else:
                # search to the right
                r = m - 1

        return res

# [3, 4, 5, 1, 2]
#  L     M     R
#       [5, 1, 2]
#        L  M  R
#          [1, 2]
#           LM  R
#           subarray is sorted in increasing order, return leftmost -> 1
