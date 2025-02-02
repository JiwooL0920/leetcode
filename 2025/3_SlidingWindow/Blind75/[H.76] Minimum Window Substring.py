# Feb 1, 2025
# https://leetcode.com/problems/minimum-window-substring/description/

# Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string ""
# Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

class Solution:
    def minWindow(self, s:str, t:str) -> str:
        if t == "": return ""

        countT, windwow = {}, {}

        # initialize countT
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('infinity')

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # just satisfied for condition for the first time
            if c in countT and window[c] == countT:
                have += 1

            while have == need:
                # update our result
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1
                # keep shrinking from the left
                # pop from the left of our winddow
                window[s[l]] -= 1
                # its possible that have and need condition is broken
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float('infinity') else ""

