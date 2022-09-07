# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# 1) brute force - triple loop 

# 2) sort input array 
# [-3,3,4,-3,1,2]
# [-3,-3,1,2,3,4]
# -3 + _ + _ = 0 
# already visited -3 in i=0 so skip i=1; eliminate duplicates 
# problem reduces to twosum ii, use l,r pointers 
# if sum > 0, decrease sum by taking r pointer to the left
# if sum < 0, increase sum by taking l pointer to the right 
# Time: O(NlogN) + O(N^2) => O(N^2) 
#         sorting, one loop to tell us the first value, second loop to solve two sum
# Space: O(1) or O(N) based on implementation of sorting algorithm/library
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue #skip duplicate

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: #skip duplicate
                        l += 1
        return res