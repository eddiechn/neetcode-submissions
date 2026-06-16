# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        def dfs(node):
            nonlocal res
            if not node:
                res += "x" + ','
            else:
                res += str(node.val) + ","
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        print(res)
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        if vals[0] == "x":
            return None
        root = vals[0]
        self.i = 0

        def dfs():
            if vals[self.i] == "x":
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()



        e