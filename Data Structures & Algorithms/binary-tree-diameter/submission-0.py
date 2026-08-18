# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):

        self.res = 0

    def maxd(self, root):

        if not root:
            return 0
        
        else:
            leftd = self.maxd(root.left)
            rightd = self.maxd(root.right)
            self.res = max(self.res, leftd+rightd)
            return 1 + max(leftd, rightd)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:


        self.maxd(root)
        return self.res

        