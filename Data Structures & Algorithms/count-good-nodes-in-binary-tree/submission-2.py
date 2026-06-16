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
                res += 1

            if node.left:
                q.append((max(maxval, node.val), node.left))

            if node.right:
                q.append((max(maxval, node.val), node.right))


        return res

            

        