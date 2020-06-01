"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    # Newick format
    # Time and Space Complexity: O(N)

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if root == None:
            return ""

        ret = []
        self.node2str(root, ret)
        return "".join(ret)


    def node2str(self, node: 'Node', ret: []):
        ret.append(str(node.val))

        if len(node.children) > 0:
            ret.append("[")
            for i in range(len(node.children)):
                self.node2str(node.children[i], ret)

                if i < len(node.children) - 1:
                    ret.append(" ")


            ret.append("]")



    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if len(data) == 0:
            return None

        return self.str2node(data, 0)[0]

    def str2node(self, data: str, pos: int) -> ('Node', int):
        val = 0
        while pos < len(data) and data[pos] >= "0" and data[pos] <= "9":
            val = val * 10 + int(data[pos])
            pos += 1

        ret = Node(val, [])

        if pos < len(data) and data[pos] == "[":
            pos += 1

            while pos < len(data) and data[pos] != "]":
                if data[pos] == " ":
                    pos += 1
                else:
                    child, pos = self.str2node(data, pos)
                    ret.children.append(child)
            pos += 1

        return ret, pos


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
