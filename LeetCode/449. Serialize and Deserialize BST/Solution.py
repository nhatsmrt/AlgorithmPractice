# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        ret = []
        self.preorder(root, ret)
        return ' '.join(ret)

    def preorder(self, node: TreeNode, ret: List[str]):
        if node is not None:
            ret.append(str(node.val))
            self.preorder(node.left, ret)
            self.preorder(node.right, ret)


    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        insertion_orders = [int(val) for val in data.split(' ') if len(val) > 0]
        root = None

        for val in insertion_orders:
            root = self.insert(root, val)

        return root

    def insert(self, node: TreeNode, val: int):
        if node is None:
            return TreeNode(val)

        if val < node.val:
            node.left = self.insert(node.left, val)
        elif val > node.val:
            node.right = self.insert(node.right, val)

        return node



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
