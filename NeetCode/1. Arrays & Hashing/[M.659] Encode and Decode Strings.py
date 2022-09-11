# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement encode and decode 

# Example 1
# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation: One possible encode method is: "lint:;code:;love:;you"

# encode ["neet","code"] -> "neetcode"
# decode "neetcode" -> ["neet","code"]
# need some kind of separator 
# ex. "neet#code"
# but problem. ["neet","co#de"] -> "neet#co#de"

# one solution: numCharBefore, numCharAfter
# but can't store it in different datastructure; must be in the string itself 
# --> always an integer in the beginning, and a single delimiter in between that integer and the actual word
# "4#neet5#co#de"
# Time: O(N)

class Solution: 
    def encode(self, strs):
        res = "" 
        for s in strs: 
            res += str(len(s)) + "#" + s 
        return res 
        
    def decode(self, str):
        res, i = [], 0
        while i < len(str):
            # j is our integer (length of the string that comes before #)
            j = i 
            while str[j] != "#":
                j += 1 
            length = int(str[i:j])
            res.append(str[j+1 : j+1+length])
            i = j + 1 + length # beginning of next string 
        return res 
            
        