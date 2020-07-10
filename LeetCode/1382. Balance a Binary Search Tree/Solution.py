# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_arr = []
        self.inorder(root, sorted_arr)

        return self.toBST(sorted_arr, 0, len(sorted_arr) - 1)

    def inorder(self, node: TreeNode, arr: List[int]):
        if node is not None:
            self.inorder(node.left, arr)
            arr.append(node.val)
            self.inorder(node.right, arr)

    def toBST(self, arr: List[int], start: int, end: int) -> TreeNode:
        if start > end:
            return None

        mid = start + (end - start) // 2
        ret = TreeNode(arr[mid])

        if start == end:
            return ret

        ret.left = self.toBST(arr, start, mid - 1)
        ret.right = self.toBST(arr, mid + 1, end)

        return ret
        
