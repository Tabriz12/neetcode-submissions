# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.res = 0

    def preOrder(self, root, maks):

        if root:

            if maks <= root.val:
                self.res+=1
            maks = max(maks, root.val)
            
            self.preOrder( root.left, maks)
            self.preOrder(root.right, maks)





    def goodNodes(self, root: TreeNode) -> int:

        self.preOrder(root, -101)

        return self.res

        
        