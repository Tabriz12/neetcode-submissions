from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()

        for a in asteroids:
            alive = True

            while stack and stack[-1] > 0 and a < 0:
                if abs(a) > abs(stack[-1]):
                    stack.pop()
                elif abs(a) == abs(stack[-1]):
                    stack.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break

            if alive:
                stack.append(a)

        return list(stack)


            





            

        