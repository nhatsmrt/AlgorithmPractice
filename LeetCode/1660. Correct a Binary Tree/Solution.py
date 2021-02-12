# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        parent = {}
        traverse_queue = collections.deque()
        traverse_queue.append(root)

        while traverse_queue:
            node = traverse_queue.popleft()

            if node.left:
                parent[node.left] = node
                traverse_queue.append(node.left)

            if node.right:
                if node.right in parent:
                    # node is the invalid one
                    if node == parent[node].left:
                        parent[node].left = None
                    else:
                        parent[node].right = None
                    break

                parent[node.right] = node
                traverse_queue.append(node.right)

        return root
