# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):

        self.res = None
    

    def dirtydeeds(self, root: TreeNode, p: TreeNode, q: TreeNode):

        if not root:
            return
        

        if root.val in [p.val, q.val] and not self.res:
            self.res = root
        
        elif (
                (root.val < q.val and root.val > p.val) or (root.val > q.val and root.val < p.val)
            ) and not self.res:

            self.res = root
        
        self.dirtydeeds(root.left, p, q)
        self.dirtydeeds(root.right, p , q)
    
    
    

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        self.dirtydeeds(root, p, q)

        return self.res



        








        