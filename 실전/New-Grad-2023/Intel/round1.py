# '''
# Given a 2d mxn grid map of 1's (land) and 0's (water), return the number of islands.
# An island is formed by connecting neighbor lands horizontally or vertically, but not diagonally.

# grid is represented by nested list:
# grid = [
#     [1, 0, 0, 0], 
#     [1, 1, 0, 0], 
#     [0, 1, 0, 1],
#     [1, 0, 1, 1]
# ]

# [0,1,2,2]
# [0,0,1,1]
# [1,0,1,0]
# [0,1,0,0]

# # follow up: find the distance of the nearest 1 for each cell.
# grid = [[1,0,0]]
# ans = [[0,1,2]]
# '''
# from collections import deque 
from collections import deque 

def solve(grid):
    ROWS, COLS = len(grid), len(grid[0])
    ans = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    def bfs(r,c):
        q = deque([(r,c)]) 
        visit = set((r,c)) 
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        res = 0
        while q:
            for i in range(len(q)):
                (row,col) = q.popleft() 
                if grid[row][col] == 1:
                    return res 
                for dr, dc in directions:
                     newR, newC = row + dr, col + dc 
                     if (newR in range(ROWS)) and (newC in range(COLS)) and ((newR, newC) not in visit):
                         q.append((newR, newC))
                         visit.add((newR, newC))
                
            res += 1
                    
        return res 


    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 0:
                d = bfs(r,c) # distance 
                ans[r][c] = d

    return ans




grid = [
    [1, 0, 0, 0], 
    [1, 1, 0, 0], 
    [0, 1, 0, 1],
    [1, 0, 1, 1]
]

[[0, 1, 2, 2],
 [0, 0, 1, 1],
 [1, 0, 1, 0],
 [0, 1, 0, 0]]

g = solve(grid)
print(g)


# # ans = solve(grid)
# # print(ans)

# # def solve(grid):
# #     ROWS, COLS = len(grid), len(grid[0])
# #     visit = set() 

# #     def dfs(r,c):
#         # if (r in range(ROWS)) and (c in range(COLS)) and ((r,c) not in visit) and (grid[r][c] == 1):
# #             visit.add((r,c))
# #             dfs(r+1, c)
# #             dfs(r-1, c)
# #             dfs(r, c+1)
# #             dfs(r, c-1) 

#     # res = 0
#     # for r in range(ROWS):
#     #     for c in range(COLS):
#     #         if grid[r][c] == 1 and ((r,c) not in visit):
#     #             res += 1 
#     #             dfs(r,c) 

#     # return res

"""
I am helping organize a fundraiser, and I'm given the task of distributing
gifts for the donors.
Donors are lined up in a straight line to receive their gifts, and I distribute
the gifts according to a couple of rules:
1. Every donor must receive at least 1 gift
2. If donors of different donation amounts are beside each other, then the
   person who donated more must receive more gifts
Return the minimum number of gifts to distribute

e.g.
donations = [27, 36, 49, 44]
(gifts = [1,2,3,1]) out = 7

donations = [44, 49, 36, 27]
gifts = [1, 2, 1, 1] l->r
r->l  [1, 3, 2, 1]

gifts = [1, 3, 2, 1]
[1, 2, 3, 2, 1]
1, 2, 3, 1, 1
1  1  3  2  1

[1, 2, 3, 4, 3, 2, 3, 5, 1, 3]
1, 2, 3, 4, 1, 1, 2, 3, 1, 2
1, 1, 2, 1, 1, 2, 3, 1, 1, 1

1,2,3,4,1,2,3,3,1,2

1,2,3,4,2,1,2,3,1,2
"""

# first, last = donation[0], donations[-1]
# donations = first + donations + last 

def get_gift_count(donations):
    out = [1 for i in range(len(donations))]
    
    # left -> right 
    for i in range(1,len(donations)):
        cur = donations[i]
        prev = donations[i-1]
        if cur > prev:
            gift_previous = out[i-1]
            out[i] += gift_previous
    
    # right -> left 
    out2 = [1 for i in range(len(donations))]
    for i in range(len(donations)-2, -1, -1):
        cur = donations[i]
        prev = donations[i+1]
        if cur > prev:
            gift_previous = out2[i+1]
            out2[i] += gift_previous

    out3 = []
    for i in range(len(out)):
        o = max(out[i], out2[i]) 
        out3.append(o)


    return (out, out2, out3)

# donations = [44, 49, 36, 27]
# ans = get_gift_count(donations)
# print(ans)
    



def get_gift_count(donations):
    out = [1 for i in range(len(donations))]
    dp = [False for i in range(len(donations))]
    
    out[0] = 2 if donations[0] > donations[1] else 1
    out[-1] = 2 if donations[-1] > donations[-2] else 1
    
    for i in range(1,len(donations)-1):
        left = donations[i-1]
        cur =  donations[i]
        right = donations[i+1]
        
        if(cur < left): dp[i] = True

        if cur > left:
            out[i] = max(out[i], out[i-1] + 1)
        if cur > right:
            out[i] = max(out[i], out[i+1] + 1)
            
    for i in range(1, len(dp) - 1):
        if(dp[i]):
            if i < len(dp) and donations[i] > donations[i + 1]:
                out[i] = max(out[i], out[i+1] + 1)
            
    return out