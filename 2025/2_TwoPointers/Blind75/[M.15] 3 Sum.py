# Jan 31, 2025
# https://leetcode.com/problems/3sum/description/

# Time: O(n^2)
# Space: O(1) or O(n), depending on the sorting algorithm used
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n1 in enumerate(nums):
            # skip same value as before - dont want to use the same value twice
            if i > 0 and n1 == nums[i-1]:
                continue
        
            # two pointer solution
            l, r = i+1, len(nums)-1
            while l < r:
                n2, n3 = nums[l], nums[r]
                summ = n1 + n2 + n3
                if summ < 0:
                    l += 1
                elif summ > 0:
                    r -= 1
                else:
                    res.append([n1, n2, n3])
                    l += 1
                    # same value, keep shifting left pointer
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
            