class TrieNode:
    def __init__(self):
        self.subtree_val = 0
        self.node_val = 0
        self.children = {}
        self.is_word = False


class MapSum:
    # Space Complexity: O(W)
    # Time Complexity: <O(1), O(L)>

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        self._insert_at(self.root, key, 0, val)

    def _insert_at(self, node, key, ind, val):
        old_val = node.subtree_val

        if ind < len(key):
            if key[ind] not in node.children:
                node.children[key[ind]] = TrieNode()

            node.subtree_val += self._insert_at(node.children[key[ind]], key, ind + 1, val)
        else:
            node.is_word = True
            node.subtree_val += val - node.node_val
            node.node_val = val

        return node.subtree_val - old_val



    def sum(self, prefix: str) -> int:
        it = self.root

        for char in prefix:
            if char not in it.children:
                return 0

            it = it.children[char]

        return it.subtree_val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
