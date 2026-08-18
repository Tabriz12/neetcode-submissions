from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        if not amount: return amount

        seen = {k: False for k in range(amount+1)}

        seen[0] = True

        q = deque([0])

        res = 0

        while q:

            res+=1

            ln = len(q)

            for _ in range(ln):

                top = q.popleft()

                for c in coins:

                    if top + c == amount:
                        return res
                    
                    elif top + c > amount or seen[top+c]:
                        continue
                    
                    else:

                        seen[top+c] = True

                        q.append(top+c)
        
        return -1
        

                    








        
        