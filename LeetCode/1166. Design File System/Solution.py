class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = {}


class FileSystem:

    def __init__(self):
        self.root = Node()


    def createPath(self, path: str, value: int) -> bool:
        components = path.split("/")[1:]
        return self.insert(self.root, components, 0, value)

    def insert(self, node: Node, components: List[str], i: int, value: int) -> bool:
        if i == len(components) - 1:
            if components[i] in node.children:
                return False
            else:
                node.children[components[i]] = Node(value)
                return True
        else:
            if components[i] not in node.children:
                return False

            return self.insert(node.children[components[i]], components, i + 1, value)

    def get(self, path: str) -> int:
        components = path.split("/")[1:]
        it = self.root

        for component in components:
            if component not in it.children:
                return -1

            it = it.children[component]

        return it.value




# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
