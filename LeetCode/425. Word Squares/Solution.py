class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        prefix = {}

        for word in words:
            for i in range(len(word)):
                if word[:i] not in prefix:
                    prefix[word[:i]] = []

                prefix[word[:i]].append(word)

        self.prefix = prefix
        ret = []
        self.backtrack([], ret)
        return ret

    def backtrack(self, cur: List[str], ret: List[List[str]]):
        if not cur:
            for word in self.prefix[""]:
                cur.append(word)
                self.backtrack(cur, ret)
                cur.pop()
        elif len(cur) == len(cur[0]):
            ret.append(copy.deepcopy(cur))
        else:
            prefix = []

            for word in cur:
                prefix.append(word[len(cur)])

            prefix = "".join(prefix)

            for word in self.prefix.get(prefix, []):
                cur.append(word)
                self.backtrack(cur, ret)
                cur.pop()
