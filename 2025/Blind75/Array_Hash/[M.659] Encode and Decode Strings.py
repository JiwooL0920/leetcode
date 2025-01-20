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
