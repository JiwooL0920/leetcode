# Feb 1, 2025
# https://leetcode.com/problems/minimum-window-substring/description/

# Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string ""
# Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

# one variable "have" to represent the total num of characters we have out of the target
# need: remaining charcter to get target
# once we find a substring (have == need), keep shrinking left window until have < need
# repeat the process to see if there is a smaller substring

# Time: O(N)
# Space: O(N)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        # count for unique characters in t
        countT = {}
        # track the number of characters in the current window
        window = {}

        # initialize countT
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")

        l = 0
        # start expanding the right window
        for r in range(len(s)):
            c = s[r]
            # update number of characters in the current window
            window[c] = 1 + window.get(c, 0)

            # see if we found a target character
            if (
                c in countT # c is target character
                and window[c] == countT[c] # required number of c required in t is met
            ):
                have += 1

            # met the requirements for target string
            while have == need:
                # found a new candidate, see if we can update min window
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = (r-l+1)

                # pop from the left of our window
                window[s[l]] -= 1

                # update have count if we need to
                # when we move l to shrink the window, we are removing s[l] from the current window
                # if s[l] is a target character
                # and we remove one occurrence below the required count, we must decrease have
                if (
                    s[l] in countT # it was a target character
                    and window[s[l]] < countT[s[l]] # count of char in current window went below number of chars required in target
                ):
                    have -= 1
                # shift left window by 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
