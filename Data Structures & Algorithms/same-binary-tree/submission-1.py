# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:



        def check(p, q):


            if not p and not q:
                return True
            
            elif (p and not q) or (q and not p) or (p.val != q.val):

                return False
            

            else:
                
                if not check(p.left, q.left):

                    return False
                    
                    
                elif not check(p.right, q.right):

                    return False

                return True
        
        return check(p, q)
                

            


            



        


        


        
        