# 01/25/2025
# Time: O(N), Space: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            summ = numbers[l] + numbers[r]
            if summ < target:
                l += 1
            elif summ > target:
                r -= 1
            else:
                # indices are based on 1, so add 1
                return [l+1, r+1] 
        return [] 

# -----------------------------------------------------------------------
# Review: Feb 8, 2025
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            n1, n2 = numbers[l], numbers[r]
            summ = n1 + n2
            if summ < target:
                l += 1
            elif summ > target:
                r -= 1
            else:
                return [l+1, r+1]