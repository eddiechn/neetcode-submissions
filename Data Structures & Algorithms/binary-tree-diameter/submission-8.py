# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def height(root):
            if not root:
                return 0

            self.res = max(self.res, height(root.left) + height(root.right))

            return 1 + max(height(root.left), height(root.right))
        if not root:
            return 0

        height(root)

        return self.res



        def height(root):
            if not root:
                return 0

            self.res = max(self.res, height(root.left) + height(root.right))

            return 1 + max(height(root.left), height(root.right))
        