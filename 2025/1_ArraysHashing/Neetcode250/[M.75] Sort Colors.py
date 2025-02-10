# Feb 10, 2025
# https://leetcode.com/problems/sort-colors/

# Time: O(N)
# Space: O(1)

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        i = 0

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= r:
            # swap with left pointer
            if nums[i] == 0:
                swap(l, i)
                l += 1
            # swap with right pointer
            elif nums[i] == 2:
                swap(r, i)
                r -= 1
                i -= 1 # for i pointer, dont need to increment i
            i += 1


'''
[2, 0, 2, 1, 1, 0]
Li              R

[0, 0, 2, 1, 1, 2]
Li           R

[0, 0, 2, 1, 1, 2]
    Li       R

[0, 0, 2, 1, 1, 2]
       Li    R

[0, 0, 1, 1, 2, 2]
       Li R

[0, 0, 1, 1, 2, 2]
       L  iR
'''