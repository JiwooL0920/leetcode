# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

# 1 -> 3
# 2 -> 2
# 3 -> 1 

# sort by number of occurrences 
# or 
# put it in max heap where the key is the count  
# heapify O(N), pop O(k x logN)  k times 

# better solution: bucket sort 
# Time: O(N)
# Memory: O(N)  hashmap 
# [1,1,1,2,2,100]     len(arr) proportional so linear time 
# i(count)    0   |   1   |   2   |   3   |   4   |   5   |   6  
# values            [100]    [2]     [1]
# top 2 --> [2,1]

class Solution:
    def topKFrequent(self, nums, k):
        count = {} 
        # initialize the frequency array where index = # occurrences 
        freq = [[] for i in range(len(nums) + 1)]
        # find # of occurrences of each num in the array 
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # update the frequency list 
        #  key value 
        for n, c in count.items(): 
            freq[c].append(n)  
        # descending order --> most frequent to least frequent 
        res = [] 
        for i in range(len(freq)-1, 0, -1): 
            for n in freq[i]: 
                res.append(n)
                if len(res) == k:
                    return res 
        
        
        
# ========================    
# my own solution 
# [try 1]     
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = [[] for i in range(len(nums)+1)]
        # {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
        
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for key,val in count.items():
            freq[val].append(key)
            
        res = []
        # print(freq)
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res 
                