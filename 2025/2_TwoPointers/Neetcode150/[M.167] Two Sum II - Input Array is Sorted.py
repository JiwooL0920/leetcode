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
