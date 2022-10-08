# ou are given an array of integers nums and an integer target.

# Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

 

# Example 1:

# Input: nums = [3,5,6,7], target = 9
# Output: 4
# Explanation: There are 4 subsequences that satisfy the condition.
# [3] -> Min value + max value <= target (3 + 3 <= 9)
# [3,5] -> (3 + 5 <= 9)
# [3,5,6] -> (3 + 6 <= 9)
# [3,6] -> (3 + 6 <= 9)
# Example 2:

# Input: nums = [3,3,6,8], target = 10
# Output: 6
# Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
# [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
# Example 3:

# Input: nums = [2,3,3,4,6,7], target = 12
# Output: 61
# Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
# Number of valid subsequences (63 - 2 = 61).

# on sorted array
# [3,3,6,8] t = 10 
#  _ _ _
# 2 characters after minimum 
# i = 0, 3 (3) (6)
# we can have 2^2 subsequnce [3], [3,3], [3,3,6], [3,6]
# i = 1, 3 (6)
# we can have 2^1 subsequence [3], [3,6]
# i = 2, 6  --> can't have any more number such that sum <= target
# res = 2^2 + 2^1 = 6   we can get total 6 subarrays 
class Solution:
    def numSubseq(self, nums, target):
        ans=0
        nums.sort()
        i,j=0,len(nums)-1
        mod = 10**9 + 7
        while(i<=j):
            if nums[i]+nums[j]<=target:
                ans+=pow(2,(j-i),mod)
                i+=1
            else:
                j-=1
        return ans%mod
    
    
class Solution:
    def numSubseq(self, nums, target):
        nums.sort()
        res = 0 
        mod = (10**9 + 7)
        
        r = len(nums) - 1
        for i, left in enumerate(nums):
            while (left + nums[r]) > target and i <= r:
                r =- 1 
            if i <= r: 
                res += (2**(r - i))
                res %= mod
        
        return res 