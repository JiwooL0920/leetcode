# For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

# Given strings sequence and word, return the maximum k-repeating value of word in sequence.

# "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
# "aaaba"
# out:5

class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        count = 1
        while count * word in sequence:
            count += 1 
        return count-1