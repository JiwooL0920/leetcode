# 21:11 1/20/2025
# https://leetcode.com/problems/product-of-array-except-self/submissions/1515231176/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1) Use prefix/postfix arrays
        # get product before/after each value, and multiply by itself
        # arr: [1, 2, 3, 4]
        # pre: [1, 2, 6, 24]
        # post: [24, 24, 12, 4]
        # res: [1*24, 1*12, 2*4, 6*1] = [24, 12, 8, 6]
        # Time: O(N), Space: O(N)
        
        # 2) Better: dont need pre/post, just store directly on res
        # calculate prefix ->
        # pre: [1(default), 1*1, 1*2, 2*3] = [1, 1, 2, 6]
        # <- calculate postfix + multiply by whats already in the position
        # post: [1*24, 1*12, 2*4, 6*1]
        # Time: O(N), Space: O(1)
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

# -----------------------------------------------------------------------
# Review: Feb 8, 2025
# Time: O(N), Space: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #   [1,  2,  4, 6]
        # ----------------------
        # 1 [   1,      (1x1),   (1x1x2), (1x2x4) ]   prefix 
        #   [(2x4x6x1), (4x6x1), (6x1),      1    ]   postfix
        # ----------------------
        # 1 [1,  1,  2,  8]       prefix
        #   [48, 24, 6,  1] 1     postfix
        # ---------------------(x)
        # = [48, 24, 12, 8]
        lenn = len(nums)
        result = [1 for i in range(lenn)]

        prefix = 1
        for i in range(lenn):
            result[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(lenn-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result
