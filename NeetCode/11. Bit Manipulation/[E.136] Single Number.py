# Non empty array. every elem appears twice wxcept for one. fine single value in T O(N) and M O(1)

# old solution
class Solution(object):
    def singleNumber(self,nums):
        # O(N) time 
        # O(N) space
        d = dict() 
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
                
        for n in d:
            if d[n] == 1:
                return n 
            
        return -1 

    
"""
Test Case: [4,1,2,1,2]
------------------------
<< FIRST FOR LOOP >>
iteration 0:
	d = {} 
	n = 4
	n not in d --> add n to d 
	d = {4:1}
iteration 1:
	d = {4:1}
	n = 1
	n not in d --> add n to d 
	d = {4:1, 1:1}
iteration 2:
	d = {4:1, 1:1}
	n = 2
	n not in d --> add n to d 
	d = {4:1, 1:1, 2:1}
iteration 3:
	d = {4:1, 1:1, 2:1}
	n = 1 
	n in d. increase value by 1 
	d = {4:1, 1:2, 2:1}
iteration 4:
	d = {4:1, 1:2, 2:1}
	n = 2 
	n in d. increase value by 1 
	d = d = {4:1, 1:2, 2:2}
------------------------
<< SECOND FOR LOOP >>
iteration 0:
	key = 4
	value = 1 --> found. return key 
------------------------
output: 4 
"""


# neetcode
class Solution:
    def singleNumber(self, nums):
        res = 0
        for n in nums:
            res = n ^ res 
        return res 