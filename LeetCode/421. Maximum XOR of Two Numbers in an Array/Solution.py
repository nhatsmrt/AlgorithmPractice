class TrieNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Trie:
    def __init__(self):
        self.root = TrieNode(-1)
        self.powers = [(2 ** i) for i in range(31)][::-1]

    def add(self, num) -> int:
        rep = bin(num)[2:]
        if len(rep) < 31:
            rep = ''.join(['0' for i in range(31 - len(rep))]) + rep

        it_add = self.root
        it_max = self.root
        ret = 0

        for i in range(len(rep)):
            if rep[i] == '0':
                if it_add.left is None:
                    it_add.left = TrieNode(0)
                it_add = it_add.left

                if it_max.right is None:
                    it_max = it_max.left
                else:
                    it_max = it_max.right
                    ret += self.powers[i]

            else:
                if it_add.right is None:
                    it_add.right = TrieNode(1)
                it_add = it_add.right

                if it_max.left is None:
                    it_max = it_max.right
                else:
                    it_max = it_max.left
                    ret += self.powers[i]
        return ret

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Time + Space Complexity: O(n)
        trie = Trie()
        ret = 0
        for num in nums:
            ret = max(ret, trie.add(num))
        return ret
