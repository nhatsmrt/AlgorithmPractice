import re

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ret = []
        index = {}
        content_pattern = re.compile(r'\([a-zA-Z0-9]+\)')
        filename_pattern = re.compile(r'[a-z1-9]+.txt')

        for path in paths:
            information = path.split(" ")
            root = information[0]

            for i in range(1, len(information)):
                filename = filename_pattern.search(information[i]).group(0)
                content = content_pattern.search(information[i]).group(0)[1:-1]

                fullpath = root + "/" + filename
                if content not in index:
                    index[content] = []
                index[content].append(fullpath)
        for content in index:
            if len(index[content]) > 1:
                ret.append(index[content])
        return ret
