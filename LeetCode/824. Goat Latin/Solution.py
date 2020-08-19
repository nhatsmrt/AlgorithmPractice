from itertools import starmap


class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(" ")
        return " ".join(starmap(self.process, enumerate(words)))

    def process(self, index: int, word: str) -> str:
        ret = []
        if word[0].lower() in ("a", "e", "i", "o", "u"):
            ret.append(word)
        else:
            ret.append(word[1:])
            ret.append(word[0])

        ret.append("ma")
        ret.extend(["a" for i in range(index + 1)])

        return "".join(ret)
