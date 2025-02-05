# Feb 4, 2025
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        # binary search
        while l <= r:
            mid = (l+r) // 2
            # found the value, return it
            if target == nums[mid]:
                return mid
            # we are in the left sorted portion
            if nums[l] <= nums[mid]:
                # search right
                if (
                    target > nums[mid]
                    or target < nums[l]
                ):
                    l = mid + 1
                # search left
                else:
                    r = mid - 1
            # we are in the right sorted portion
            else:
                # search left
                if (
                    target < nums[mid]
                    or target > nums[r]
                ):
                    r = mid - 1
                # search right
                else:
                    l = mid + 1
        return -1

