# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Morris traversal:

        cur = root
        pred = None # true predecessor of a node
        first = None
        second = None

        while cur:
            if cur.left:
                it = cur.left
                while it.right and it.right != cur:
                    it = it.right

                if not (it.right):
                    it.right = cur
                    cur = cur.left
                else:
                    # cur has been previously traversed
                    # going right

                    # check true predecessor and cur:
                    if pred and pred.val > cur.val:
                        second = cur

                        if first is None:
                            first = pred


                    pred = cur
                    it.right = None
                    cur = cur.right
            else:
                # going right:
                if pred and pred.val > cur.val:
                    second = cur

                    if first is None:
                        first = pred

                pred = cur
                cur = cur.right

        print(first, second)
        (first.val, second.val) = (second.val, first.val)
