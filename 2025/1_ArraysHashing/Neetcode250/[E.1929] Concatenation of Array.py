# Feb 9, 2025
# https://leetcode.com/problems/concatenation-of-array/

# Time: O(N)
# Space: O(1) not counting result arr, or O(2*N)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lenn = len(nums)
        res = [0] * (2*lenn)

        for i in range(lenn):
            res[i] = nums[i]
            res[i+lenn] = nums[i]

        return res

# Neetcode solution
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i, num in enumerate(nums):
            ans[i] = ans[i + n] = num
        return ans
