# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        if not root: return res

        q = deque([root])

        while q:

            ln = len(q)
            lvl = []
            for _ in range(ln):

                top = q.popleft()

                lvl.append(top.val)

                if top.left:
                    q.append(top.left)
                
                if top.right:
                    q.append(top.right)
            
            res.append(lvl)
        
        return res








        