class Solution:
    def generate(self, numRows: int) -> List[List[int]]:


        res = [[1]]



        for i in range(1,numRows):


            last = res[-1]

            new = [1] + [last[j]+last[j+1] for j in range(len(last)-1)] + [1]

            res.append(new)
        
        return res


        
        