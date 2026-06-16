# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        if not root:
            return None

        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                nodes.append(node.val)



        nodes.sort()
        return nodes[k - 1]

        