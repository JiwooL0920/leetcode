# Feb 15, 2024
# https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapp = {}
        for i, n in enumerate(nums):
            if n in mapp:
                if abs(mapp[n]-i) <= k:
                    return True
            mapp[n] = i
        return False
     
        