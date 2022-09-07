# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

# 1) sorted 
# Time: O(NlogN) --> not efficient 

# 2) 
# each sequence has a start value (no left neighbour)
# make array into a set 
# check if it has a left neighbour
# count how many consequtive neighbours in the set  
# 100 -> 
# 200 ->
# 1 -> 2- > 3 -> 4 -> 
# Time: O(N)
# Memory: O(N)

class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0 
        for n in nums: 
            # check if it's the start of a sequence 
            if (n-1) not in numSet: 
                length = 0
                while (n + length) in numSet:
                    length += 1 
                longest = max(length, longest)
        return longest 
 