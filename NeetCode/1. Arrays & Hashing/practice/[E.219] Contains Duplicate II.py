# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashMap = {}
        for i, n in enumerate(nums):
            if n in hashMap:
                if abs(hashMap[n] - i) <= k:
                    return True 
            hashMap[n] = i 
        return False