#http://web.archive.org/web/20060926225645/http://www.cs.uku.fi/~kilpelai/BSA05/lectures/slides04.pdf
# Actually REALLY slow
from collections import deque


class ACNode:
    def __init__(self, char: str, is_root: bool=False):
        self.char, self.is_root = char, is_root
        self.outputs = set() # indices of matched patterns
        self.fail = None # ACNode
        self.goto_map = {}  # char -> ACNode

    def goto(self, char: str):
        if self.is_root:
            return self.goto_map.get(char, self)

        return self.goto_map.get(char, None)


class ACAutomaton:
    def __init__(self, words: List[str]):
        self.root = ACNode("$$", True)
        self.words = words
        self.alphabet = set([char for word in words for char in word])

        for i in range(len(words)):
            self.add_word(i)

        queue = deque()
        for char in self.alphabet:
            node = self.root.goto(char)
            if node != self.root:
                node.fail = self.root
                queue.append(node)

        while len(queue) > 0:
            node = queue.popleft()
            for char in self.alphabet:
                next_node = node.goto(char)
                if next_node is not None:
                    queue.append(next_node)
                    it = node.fail
                    while it.goto(char) is None:
                        it = it.fail
                    next_node.fail = it.goto(char)
                    for label in it.goto(char).outputs:
                        next_node.outputs.add(label)

    def add_word(self, i: int):
        word = self.words[i]
        it = self.root
        for char in word:
            if char not in it.goto_map:
                it.goto_map[char] = ACNode(char)
            it = it.goto_map[char]
        it.outputs.add(i)

    def search_text(self, text: str) :
        ret = {}
        it = self.root

        for i in range(len(text)):
            char = text[i]
            while it.goto(char) is None:
                it = it.fail
            it = it.goto(char)
            if len(it.outputs) > 0:
                for match in it.outputs:
                    if match not in ret:
                        ret[match] = []
                    ret[match].append(i - len(self.words[match]) + 1)

        return ret


class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        ac_aut = ACAutomaton(dict)

        occurences = ac_aut.search_text(s)
        events = []
        for i in occurences:
            for occurence in occurences[i]:
                events.append((occurence, True))
                events.append((occurence + len(dict[i]), False))

        events.sort(key=lambda t: t[0])
        num_opening = 0
        text_ind = 0
        ret = []
        for i in range(len(events)):
            event = events[i]
            if event[1]:
                if num_opening == 0:
                    for j in range(text_ind, event[0]):
                        ret.append(s[j])
                    # print(i)
                    if i == 0 or events[i - 1][0] != events[i][0]:
                        ret.append("<b>")
                    text_ind = event[0]
                num_opening += 1
            else:
                if num_opening == 1:
                    for j in range(text_ind, event[0]):
                        ret.append(s[j])
                    if i == len(events) - 1 or events[i + 1][0] != events[i][0]:
                        ret.append("</b>")
                    text_ind = event[0]
                num_opening -= 1

        ret.append(s[text_ind:])
        return ''.join(ret)

    def find(self, text: str, pattern: str):
        ret = []
        i = 0
        while i < len(text) and i >= 0:
            occur = text[i:].find(pattern)
            if occur >= 0:
                ret.append(occur + i)
                i = occur + i + 1
            else:
                break
        return ret
