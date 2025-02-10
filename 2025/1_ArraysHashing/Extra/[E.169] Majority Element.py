# Feb 10, 2025
# https://leetcode.com/problems/majority-element/description/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(N)
        # Space: O(1)
        res, count = 0, 0

        for n in nums:
            # set first element to majority element
            if count == 0:
                res = n

            # increment count by 1 if we see same number
            # decrement 1 if encountered diff number
            count += (1 if n == res else -1)
        
        return res


'''
[2, 2, 1, 1, 1, 2, 2]
 ^
res = 2, count = 1

[2, 2, 1, 1, 1, 2, 2]
    ^
res = 2, count = 2

[2, 2, 1, 1, 1, 2, 2]
       ^
res = 2, count = 1

[2, 2, 1, 1, 1, 2, 2]
          ^
res = 2, count = 0

[2, 2, 1, 1, 1, 2, 2]
             ^
res = 1, count = 1

[2, 2, 1, 1, 1, 2, 2]
                ^
res = 1, count = 0

[2, 2, 1, 1, 1, 2, 2]
                   ^
res = 2, count = 1
'''
        
        