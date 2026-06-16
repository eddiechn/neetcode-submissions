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

        q = deque()
        q.append((-float('inf'), root))
        while q:
            maxval, node = q.popleft()
            if node.val >= maxval:
                maxval = node.val
                res += 1

            if node.left:
                q.append((maxval, node.left))
            if node.right:
                q.append((maxval, node.right))


            
        


        return res
        