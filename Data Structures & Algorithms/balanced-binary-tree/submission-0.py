# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.ans = True
    
    def rec(self, root):

        if not root:

            return 0
        
        else:

            l = self.rec(root.left)
            r = self.rec(root.right)

            if abs(l-r) > 1:
                self.ans = False
            
            return 1 + max(l,r)
            

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.rec(root)
        return self.ans



        
            


                

            



        