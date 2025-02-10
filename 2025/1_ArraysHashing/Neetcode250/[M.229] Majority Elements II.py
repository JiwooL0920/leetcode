# Feb 10, 2025
# 
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # majority elements will be in this map
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
            
            if len(count) <= 2:
                continue # dont decrement count
            
            new_count = defaultdict(int)
            for n, c in count.items():
                # decrement it down to 0
                if c > 1:
                    new_count[n] = c - 1
            count = new_count
                
        res = []
        for n in count: # at most 2 elements in the hashmap
            if nums.count(n) > (len(nums) // 3):# linear time ops, but its only going to execute 2 times
                res.append(n)
        return res


'''
Input: [3, 3, 4, 2, 4, 4, 2, 4, 4]

Initial nums: [3, 3, 4, 2, 4, 4, 2, 4, 4]

1st iteration: 
count = {3: 1}

2nd iteration: 
count = {3: 2}

3rd iteration: 
count = {3: 2, 4: 1}

4th iteration: 
count = {3: 1, 4: 1, 2: 1}

5th iteration: 
count = {4: 2, 2: 1} 
(3 is discarded because count of 3 is 0)

6th iteration: 
count = {4: 3, 2: 1} 
(3 discarded again)

7th iteration: 
count = {4: 3, 2: 2} 
(final result: count of 4 > len(nums)//3)

Final result: [4] 
'''