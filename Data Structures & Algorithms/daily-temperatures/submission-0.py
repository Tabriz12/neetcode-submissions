from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = deque()

        res = [0] * len(temperatures)

        for i in range(len(res)-1, -1, -1):

            while stack and stack[-1][-1] <= temperatures[i]:

                stack.pop()
            
            if stack:

                res[i] = stack[-1][0] - i
            
            stack.append([i, temperatures[i]])
        
        return res
            





        