# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# 1) prefix & postfix 
# multiply every value before n (prefix) and after n (postfix), then multiply them 
# arr     [1,  2,  3,  4]
# prefix  [(1x1),(1x2),(2x3),(4x6)]       default 1 index start and end 
#         [1,  2,  6,  24]    
# postfix [(1x24),(2x12),(3x4),(4x1)]
#         [24, 24, 12, 4]
# output  [(1x24),(2x12),(2x4),(6x1)]
#         [24,24,12,4]
# but we don't have to use extra memory for prefix and postfix arrays 
# we do two passes on input array
# 1) start -> end, compute prefix and store in index(n)+1 
#   output [1,1,2,6]
# 2) end -> start, compute postfix and multiply in index(n)-1 
# default 1 at the very beginning and end 
#   output [(1x24),(1x12),(2x4),(6x1)]
#          [24,12,8,6]

class Solution:
    def productExceptSelf(self, nums):
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