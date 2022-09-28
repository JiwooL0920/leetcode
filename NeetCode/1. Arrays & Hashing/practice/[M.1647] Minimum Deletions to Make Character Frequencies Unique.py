# A string s is called good if there are no two different characters in s that have the same frequency.

# Given a string s, return the minimum number of characters you need to delete to make s good.

# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

 

# Example 1:
# Input: s = "aab"
# Output: 0
# Explanation: s is already good.

# Example 2:
# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

# Example 3:
# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

# count number of frequencies in a map 
# use set for unique frequencies 
# Iterate on the alphabet characters, keep decreasing the frequency of the current character until it reaches a value that has not appeared before.

# T: O(N)
# M: O(N)

from collections import defaultdict 

class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        mymap = defaultdict(int)
        for c in s:
            mymap[c] += 1 
        
        unique = set()
        res = 0 
        for freq in mymap.values():
            while freq > 0 and freq in unique:
                freq -= 1 
                res += 1
            unique.add(freq)
        return res