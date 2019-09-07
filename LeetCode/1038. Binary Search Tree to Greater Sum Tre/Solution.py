# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        root = self.bstToGstHelper(root, 0)
        root.smaller = None
        return root

    def bstToGstHelper(self, root: TreeNode, from_above: int):
        if (root == None):
            return root;

        root.right = self.bstToGstHelper(root.right, from_above)
        if (root.right != None):
            # print(str(root.right.val) + "_" + str(root.right.smaller))
            from_above = root.right.val + root.right.smaller
            root.right.smaller = None

        from_above += root.val
        root.val = from_above
        if (root.left != None):
            root.left = self.bstToGstHelper(root.left, from_above)
            root.smaller = (root.left.val - from_above) + root.left.smaller
            root.left.smaller = None
        else:
            root.smaller = 0
        return root
        
