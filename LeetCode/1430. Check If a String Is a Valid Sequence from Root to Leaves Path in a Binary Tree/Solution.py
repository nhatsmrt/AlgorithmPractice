# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLeaf = False

class Trie:
    def __init__(self, tree_root: TreeNode):
        self.root = TrieNode()
        self.build(self.root, tree_root)

    def build(self, trie_node: TrieNode, tree_node: TreeNode):
        if tree_node is not None:
            if tree_node.val not in trie_node.children:
                trie_node.children[tree_node.val] = TrieNode()

            trie_node = trie_node.children[tree_node.val]
            if tree_node.left is None and tree_node.right is None:
                trie_node.isLeaf = True

            self.build(trie_node, tree_node.left)
            self.build(trie_node, tree_node.right)

    def search(self, arr: List[int]) -> bool:
        it = self.root
        for num in arr:
            if num not in it.children:
                return False
            it = it.children[num]

        return it.isLeaf



class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        # Time Complexity: O(V + N)
        # Space Complexity: O(V)

        trie = Trie(root)
        return trie.search(arr)
        
