# T: O(N)
# M: O(1)

# nums[0] <= nums[1] >= nums[2] <= nums[3] 
# unsorted nums. reorder inplace


class Solution:
    def wiggleSort(self, nums):
        for i in range(1, len(nums)):
            # values at odd indices = greater than prev
            # values at even indices = less than prev 
            if (i % 2 == 1 and nums[i] < nums[i-1]) or (i % 2 == 0 and nums[i] > nums[i-1]):
                nums[i], nums[i-1] = nums[i-1], nums[i]
        return nums 
