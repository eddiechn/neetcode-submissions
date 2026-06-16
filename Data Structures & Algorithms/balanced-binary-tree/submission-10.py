# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node):
            if not node:
                return True, -1

            left_b, left_h = check_balance(node.left)
            if not left_b:
                return False, 0

            right_b, right_h = check_balance(node.right)
            if not right_b:
                return False, 0

            is_balanced = abs(left_h - right_h) <= 1
            cur_height = max(left_h, right_h) + 1


            return is_balanced, cur_height

        balanced, _ = check_balance(root)
        return balanced
        
        
        