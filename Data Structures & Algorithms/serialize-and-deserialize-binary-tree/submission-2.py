# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque([root])
        res = ""
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    res += str(node.val)
                    q.append(node.left)
                    q.append(node.right)

                else:
                    res += "x"

                res += ";"
            

        print(res)

        return res



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(';')
        root = vals[0]
        if root == "x":
            return None

        root = TreeNode(int(root))
        q = deque([root])
        index = 1
        while q:
            node = q.popleft()
            if vals[index] != "x":
                node.left = TreeNode(int(vals[index]))
                q.append(node.left)

            index += 1
            if vals[index] != "x":
                node.right = TreeNode(int(vals[index]))
                q.append(node.right)
            index += 1

        return root

        
