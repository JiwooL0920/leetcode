# 21:22 1/20/2025
# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Using set
        # Time: O(N), Space: O(N)
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            # check if its the start of a sequence
            # (if it doesnt have a left neighbour)
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest

# -----------------------------------------------------------------------
# Review: Feb 8, 2025
# Wrong answer, but if question were to find the longest consequtive sequence existing
# Time: O(N), Space: O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 

        i = 0
        while i < len(nums):
            streak = 1
            j = i+1
            while j < len(nums) and nums[j]-nums[i] == 1:
                streak += 1
                j += 1
                i += 1
            res = max(res, streak)
            i = j+1
        
        return res 