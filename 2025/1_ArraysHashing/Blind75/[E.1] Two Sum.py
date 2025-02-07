# 23:05 1/19/2025
# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap
        # Time: O(N), Space: O(N)

        # 1) record val:index for each number in the list
        indices = {} # val : index
        for i, n in enumerate(nums):
            indices[n] = i

        # 2) iterate through the list again, checking if the value for target-n is there
        for i, n in enumerate(nums):
            diff = target - n
            if (
                diff in indices
                and indices[diff] != i
            ):
                return [i, indices[diff]]

# -----------------------------------------------------------------------
# Review: Feb 6, 2025
# Time: O(N), Space: O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapp:
                return [mapp[diff], i]
            mapp[n] = i

