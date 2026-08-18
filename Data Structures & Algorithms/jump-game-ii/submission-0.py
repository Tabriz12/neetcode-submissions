from collections import deque

class Solution:
    def jump(self, nums):

        q = deque([0])
        seen = {0}
        steps = 0

        while q:

            for _ in range(len(q)):

                idx = q.popleft()

                if idx >= len(nums) - 1:
                    return steps

                for jump in range(1, nums[idx] + 1):

                    nxt = idx + jump

                    if nxt not in seen and nxt < len(nums):
                        seen.add(nxt)
                        q.append(nxt)

            steps += 1