"""
........description.........
This function iterates through the characters of the string. 
When an opening bracket is encountered, it's pushed onto the stack. 
When a closing bracket is encountered, 
it checks if the stack is empty or 
if the corresponding opening bracket on top of the stack matches the current closing bracket. 
If not, it returns False. 
Finally, it returns True if the stack is empty, indicating that all brackets have been matched and closed correctly.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
    
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
            else:
                return False
    
        return not stack
