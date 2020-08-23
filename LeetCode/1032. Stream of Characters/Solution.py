class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.stream = []

        for word in words:
            self.add(word)

    def add(self, word: str):
        it = self.root
        for char in reversed(word):
            if char not in it.children:
                it.children[char] = TrieNode()
            it = it.children[char]

        it.is_word = True

    def check(self) -> bool:
        it = self.root

        for i in range(len(self.stream) - 1, -1, -1):
            char = self.stream[i]

            if char not in it.children:
                return False

            it = it.children[char]
            if it.is_word:
                return True

        return it.is_word

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        return self.check()


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False



# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
