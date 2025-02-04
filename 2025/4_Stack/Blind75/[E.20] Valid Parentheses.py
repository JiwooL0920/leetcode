# Time: O(N)
# Space: O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }
        for c in s:
            # its a closing bracket
            if c in close_to_open:
                # there is a matching open bracket
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                # opening bracket doesnt exist or doesnt match
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

