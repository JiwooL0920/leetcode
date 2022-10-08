class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        l, r = 0, len(nums) - 1 
        # reverse entire list 
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
            
        # reverse left portion (0 to k-1)
        l, r = 0, k - 1 
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        
        l, r = k, len(nums)-1
        # reverse right portion (k to end of list)
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
            
            
class Solution(object):
	def rotate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
		n = len(nums)
		k %= n
		nums[:] = nums[n - k:] + nums[:n - k]
		return nums            