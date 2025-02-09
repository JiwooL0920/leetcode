# Feb 9, 2025
# https://neetcode.io/solutions/sort-an-array

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.bubble_sort(nums) # time limit exceeded
        # return self.selection_sort(nums) # time limit exceeded
        # return self.insertion_sort(nums) # time limit exceeded
        # return self.quick_sort(nums) # mem limit exceeded

    '''
    [ Bubble Sort ]
    1. Start at the beginning of the array
    2. Compare each pair of adjacent elements
    3. If the elements are in the wrong order, swap them
    4. After each full pass through the array, the largest unsorted element bubbles up to its correct position
    5. Repeat the process for the remaining unsorted elements
    '''
    def bubble_sort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(len(nums)-1-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

    '''
    [ Selection Sort ]
    1. Start from the first element
    2. Find the smallest element in the remaining array
    3. Swap it with the first unsorted element
    4. Move to the next element and repeat the process
    ---
    Time complexity
    Best: O(N^2)
    Worst: O(N^2)
    Average: O(N^2)
    '''
    def selection_sort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)): # 1, 4
            min_index = i
            for j in range(i+1, len(nums)): # 2
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i] # 3
        return nums


    '''
    [ Insertion Sort ]
    1. Start with the second element (first element is considered sorted)
    2. Compare it with elements in the sorted portion (left side)
    3. Shift larger elements to the right
    4. Insert the current element into its correct position
    5. Repeat until the entire list is sorted
    ---
    Time complexity
    Best: O(N) - already sorted
    Worst: O(N^2) - reverse sorted
    Average: O(N^2)
    '''
    def insertion_sort(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)): # 1, 5
            for j in range(i, 0, -1): # 2
                if nums[j] < nums[j-1]: # 3, 4
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                else:
                    break # left portion is considered sorted
        return nums


    '''
    [ Quick Sort ]
    1. Choose a pivot (can be first, last, random element)
    2. Partition the array:
       2.1 Move elements smaller than the pivot to the left
       2.2 Move elements larger than the pivot to the right
    3. Recursively apply quick sort to the left and right partitions
    4. The array is sorted when all partitions are of size 1 or empty
    ---
    Time complexity
    Best: O(NlogN)
    Worst: O(N^2) - if pivot is always the smallest/largest
    Average: O(NlogN)
    '''
    def quick_sort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: # 4
            return nums

        pivot = nums[0] # 1
        tail = nums[1:]

        left = [n for n in tail if n <= pivot] # 2.1
        right = [n for n in tail if n > pivot] # 2.2

        return self.quick_sort(left) + [pivot] + self.quick_sort(right) # 3


    '''
    [ Merge Sort ]
    1. Divide the array into two halves
    2. Recursively sort the two halves
    3. Merge the two sorted halves into a single sorted array
    '''
    # def merge_sort(self, nums: List[int]) -> List[int]:
    #     if

