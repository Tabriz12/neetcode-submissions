# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):

        self.mas = -1001


    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        

        def postOrder(root):


            if root:

                a = postOrder(root.left)
                b = postOrder(root.right)

                cur = max(0, a) + max(0, b) + root.val

                mini = max(min(a, b), 0)

                self.mas = max(cur, self.mas)

                return cur - mini
                
                
            
            else:
                return 0
        
        postOrder(root)
        
        return self.mas
        

                

                








        