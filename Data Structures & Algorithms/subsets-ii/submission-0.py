class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:


        res = [[]]
        nums.sort()


        def backtrack(ops, path):

            for idx, n in enumerate(ops):

                if idx > 0 and ops[idx-1] == n:
                    continue
                
                res.append(path + [n])

                if idx < len(ops)-1:

                    backtrack(ops[idx+1:], path + [n])
        
        backtrack(nums, [])
        return res
                



            



        