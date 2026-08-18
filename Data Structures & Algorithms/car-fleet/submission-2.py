class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        if len(speed) == 1: return 1
        order = [ (target-p)/s for p, s in sorted(zip(position, speed), reverse=True)]

        
        stack = deque()
        for i in range(len(order)):

            if not stack or order[i] > stack[-1]:

                stack.append(order[i])

        return len(stack)

        