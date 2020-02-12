from typing import Optional


class Node:
    def __init__(self, name: str, is_file: bool):
        self.content = ""
        self.name = name
        self.children = {}
        self.is_file = is_file


class FileSystem:
    def __init__(self):
        self.root = Node("/", False)


    def ls(self, path: str) -> List[str]:
        res = self.iterate(path)
        if res.is_file:
            return [res.name]
        else:
            return sorted(list(self.iterate(path).children))


    def mkdir(self, path: str) -> None:
        self.iterate(path, False)


    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.iterate(filePath, True)
        node.content += content


    def readContentFromFile(self, filePath: str) -> str:
        return self.iterate(filePath).content


    def iterate(self, path: str, is_file: Optional[bool]=None) -> Node:
        path_list = path.split("/")
        it = self.root
        for next_dir in path_list:
            if len(next_dir) > 0:
                if next_dir not in it.children:
                    it.children[next_dir] = Node(next_dir, False)
                it = it.children[next_dir]
        if is_file is not None:
            it.is_file = is_file
        return it


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
