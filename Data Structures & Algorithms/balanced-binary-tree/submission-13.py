# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node): # balanced, height
            if not node:
                return True, 0

            balanced_left, height_left = dfs(node.left)
            if not balanced_left:
                return False, 0

            balanced_right, height_right = dfs(node.right)
            if not balanced_right:
                return False, 0

            if abs(height_left - height_right) > 1:
                balanced = False

            else:
                balanced = True
            
            height = 1 + max(height_left, height_right)

            return balanced, height


        return dfs(root)[0]
        

        