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

# -----------------------------------------------------------------------
# Review: Feb 11, 2025
# Time: O(N), Space: O(N)
# You can avoid additional memory by using two pointer approach above and calculating l/rmax on res on the fly (see above)
class Solution:
    def trap(self, height: List[int]) -> int:
        lmax, rmax = [0] * len(height), [0] * len(height) 
        ll, rr = 0, 0

        for i, h in enumerate(height):
            ll = max(ll, height[i])
            lmax[i] = ll

        for i in range(len(height)-1, -1, -1):
            rr = max(rr, height[i])
            rmax[i] = rr

        trappable = 0
        for i in range(len(height)-1):
            trappable += min(lmax[i], rmax[i]) - height[i]
        
        return trappable