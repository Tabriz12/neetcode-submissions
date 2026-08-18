# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):

        self.last = float('-inf')
        self.ans = True

    def inorder(self, root,):

        if root:

            self.inorder(root.left)


            if root.val <= self.last:
                self.ans = False
            
            self.last = root.val

            self.inorder(root.right)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.inorder(root)

        return self.ans
        