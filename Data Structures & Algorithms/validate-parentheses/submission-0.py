from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()


        op = ['{', '(', '[']
        cl = ['}', ')', ']']

        for c in s:

            if c in op:
                stack.append(c)
            
            
            elif not stack or op.index(stack.pop()) != cl.index(c):
                return False
        
        return not stack




        