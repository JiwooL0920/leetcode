# Jan 31, 2025
# https://leetcode.com/problems/container-with-most-water/description/

# Time: O(N)
# Space: O(1)

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights)-1

        while l < r:
            w = r-l
            hl, hr = heights[l], heights[r]
            h = min(hl, hr)
            max_area = max(max_area, w*h)

            if hl <= hr:
                l += 1
            else:
                r -= 1
        
        return max_area

# -----------------------------------------------------------------------
# Review: Feb 11, 2025
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights)-1

        while l < r:
            width = r-l
            hl, hr = heights[l], heights[r]
            height = min(hl, hr)
            area = width * height
            res = max(res, area)

            if hl <= hr:
                l += 1 
            else:
                r -= 1
            
        return res 