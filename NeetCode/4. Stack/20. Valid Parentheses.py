# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example:
# Input: s = "()[]{}"
# Output: true

# old solution i did 
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s: 
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False 
                prev = stack.pop()
                if c == ')' and prev != '(':
                    return False 
                if c == ']' and prev != '[':
                    return False 
                if c == '}' and prev != '{':
                    return False 
        return len(stack) == 0
            
# Need code 
# Time: O(N)
# Space: O(N)

class Solution:
    def isValid(self, s):
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}
        for c in s: 
            if c in closeToOpen: 
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False 
            else: 
                stack.append(c)
        return True if not stack else False 