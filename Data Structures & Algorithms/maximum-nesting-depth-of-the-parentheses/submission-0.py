class Solution:
    def maxDepth(self, s: str) -> int:


        cur = 0
        mas = 0

        for c in s:

            if c == "(":
                cur+=1
                mas = max(cur,mas)


            elif c == ")":
                cur-=1
        
        return mas
        