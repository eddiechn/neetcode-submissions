# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return 0

        q = deque([(float('-inf'), root)])    


        while q:
            maxval, node = q.popleft()
            if node.val >= maxval:
                res += 1
                maxval = node.val

            if node.left:
                q.append((maxval, node.left))

            if node.right:
                q.append((maxval, node.right))


        return res

        