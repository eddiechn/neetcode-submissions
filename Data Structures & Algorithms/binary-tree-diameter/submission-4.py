# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    h = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.height(root)
        return self.h


        




    def height(self, root) -> int:
        if not root:
            return 0

        self.h = max(self.h, self.height(root.left) + self.height(root.right))


        return max(self.height(root.left), self.height(root.right)) + 1
        