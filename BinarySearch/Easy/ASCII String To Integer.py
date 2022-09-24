# You are given a string s containing digits from "0" to "9" and lowercase alphabet characters. Return the sum of the numbers found in s.
class Solution:
    def solve(self, s):
        def isNumeric(n):
            return ord("0") <= ord(n) <= ord("9")

        res = 0
        l, r = 0, 0
        while r < len(s):
            # shift l until l is at numeric char
            while l < len(s) and not isNumeric(s[l]):
                l += 1
            # l hit the end 
            if l == len(s):
                break
            r = l 
            # shift r until r hits the end of numeric streak
            while r < len(s) and isNumeric(s[r]):
                r += 1
            num = s[l:r]
            print(l,r)
            print(num)
            res += int(num)
            l = r

        return res
            




        