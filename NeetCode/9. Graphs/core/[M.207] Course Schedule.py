# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.

# DFS
# adjacency list (hashmap): preMap 
# courses: prerequisites[]
# [[0,1],[0,2],[1,3],[1,4],[3,4]]
# crs, pre
# 0 [1,2]
# 1 [3,4]
# 2 []
# 3 [4]
# 4 [] 

# Time: O(N + P) --> O(N) 
class Solution:
    def canFinish(self, numCourses, prerequisites):
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # visitSet = all courses along the curr DFS path 
        visitSet = set() 
        def dfs(crs):
            # detected a loop, course cannot be completed
            if crs in visitSet:
                return False
            # course has no prereq
            if preMap[crs] == []:
                return True 
            visitSet.add(crs)
            # check if all prerequesites can be taken 
            for pre in preMap[crs]:
                if not dfs(pre): 
                    return False 
                # it's a course that can be taken. remove from visit set 
                visitSet.remove(crs)
                preMap[crs] = [] #we know that crs can be taken. so compress premap to empty list 
                return True 
        
        for crs in range(numCourses):
            if not dfs(crs): return False 
        
        return True 
        
