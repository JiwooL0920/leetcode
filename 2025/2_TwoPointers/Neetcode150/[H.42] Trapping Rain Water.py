# Jan 31, 2025
# https://leetcode.com/problems/trapping-rain-water/description/

# keep a record of max height left/right of the position
# Max water you can trap is min(L,R) - height, and we dont count negativse (treat as 0) 
# Time: O(N), Space: O(1) with two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                # technically it won't be negative because we do max calculation above
                res += leftMax - height[l] 
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res