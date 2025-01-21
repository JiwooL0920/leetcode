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