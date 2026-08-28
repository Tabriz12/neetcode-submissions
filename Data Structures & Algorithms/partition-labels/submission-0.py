class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_seen = {}

        for i,c in enumerate(s):

            last_seen[c] = i
        

        end = cnt = 0

        res = []

        for i, c in enumerate(s):
            
            cnt+=1

            end = max(end, last_seen[c])

            if end == i:

                res.append(cnt)
                cnt = 0
        
        return res


