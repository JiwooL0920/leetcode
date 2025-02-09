# 16:49 1/20/2025
# https://leetcode.com/problems/encode-and-decode-strings/description/

# Add a delimiiter to specify how many characters are in the string
# ex. ["neet", "co#de"] -> "4neet5co#de"
# Encode and Decode: Time: O(n), Space: O(n)

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # agreed encoding: 4#neet
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # i represents which index it's in the string now
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            # how many following characters we need to read after j(#) to get the char
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res

# -----------------------------------------------------------------------
# Review: Feb 9, 2025
# Time: O(n), Space: O(n)
class Solution:
    # ["neet", "code", "love", "you"]
    # "4#neet4#code4#love#you"
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print("encoded: ", res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        lenn = ""

        i = 0
        while i < len(s):
            c = s[i]
            # 1) if c is a number
            if ord('0') <= ord(c) <= ord('9'):
                lenn += c
                i += 1
                continue

            # 2) c is not a number
            # skip the '#'
            i += 1

            # now, c is at the start of string
            strr = s[i:i+int(lenn)]
            res.append(strr)

            # increment to the start of next encrypted string, and reset lenn
            i += int(lenn)
            lenn = ""

        return res


