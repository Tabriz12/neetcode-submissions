# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:


        res = []

        if not root:
            return res
        
        q = deque([root])

        while q:

            ln = len(q)
            lst = None
            for _ in range(ln):

                top = q.popleft()
                lst = top.val

                if top.left:

                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            
            res.append(lst)
        
        return res




        





        