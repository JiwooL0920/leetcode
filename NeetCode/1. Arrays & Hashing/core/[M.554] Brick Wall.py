# countGap (hashmap) of every single row 
# key = pos 
# val = count of gaps (in all rows)
# at the end find max val --> maximize number of gaps 
# take total number of rows - number of gaps = total number of bricks we need to cut (result)

class Solution:
    def leastBricks(self, wall):
        countGap = {0:0} # mapping pos : count of brick gaps
        
        for r in wall: 
            total = 0 # position
            for b in r[:-1]: # dont count gap at the right most wall 
                total += b 
                countGap[total] = 1 + countGap.get(total, 0)
        
        return len(wall) - max(countGap.values())