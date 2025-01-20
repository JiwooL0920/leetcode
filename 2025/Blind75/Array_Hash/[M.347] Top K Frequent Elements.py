# 00:06 1/20/2025
# https://leetcode.com/problems/top-k-frequent-elements/

# 1) Sorting
# Time: O(NlogN), Space: O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map  <number:frequency>
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
    
        # sort by frequency
        arr = []
        for n, c in count.items():
            arr.append([c, n])
        arr.sort()

        # return top k frequent elements
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
    

    

# 2) Heap:
# Heap = special tree-based DS
# Min Heap = for any node i, value of i <= values of its children (smallest element on the root)
# Max Heap = for any node i, value of i >= values of its children (largest element on the root)
# Python 'heapq' = min heap by default
# Time: O(NlogK), Space: O(N+K)
# N = length of array, K = # of top frequent elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map <number:frequency>
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        count.get(n, 0)

        # use a keep track of the top k elements
        # - maintain a heap of size k to store top k frequent elements
        heap = [] # min heap
        for n in count.keys(): # iterate through each k-v pair <n:freq> in count dict
            # push each pair <freq:n> onto heap
            # ensures that the heap is ordered by frequency 
            heapq.heappush(heap, (count[n], n)) 
            # if the size of heap exceeds k, we remove the smallest element (root of heap)
            # ensures that the heap only contains top k frequent elements
            if len(heap) > k:
                heapq.heappop(heap)
        
        # pop top k frequent elements
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
    

# 3) Bucket Sort
# Bucket Sort = divide the range of input values into "buckets", then distribute the input values into the buckets
# Time: O(N), Space: O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k:int) -> List[int]:
        # map <number:frequency>
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # create a list of empty lists where the index represents the frequency
        freq = [[] for i in range(len(nums) + 1)]
        # populate frequency buckets (place each element in the bucket corresponding to its frequency)
        for n, cnt in count.items():
            # iterate through count dictionary
            # append the element n to the list at index cnt in the freq list
            freq[cnt].append(n)
        
        # collect top k frequent elements
        res = []
        # iterate through freq list in reverse order (highest -> lowest frequency)
        for i in range(len(freq)-1, 0, -1):
            # for each non-empty list in freq, append its elements to res
            for n in freq[i]:
                res.append(n)
                # if length to res reaches k, return res
                if len(res) == k:
                    return res
