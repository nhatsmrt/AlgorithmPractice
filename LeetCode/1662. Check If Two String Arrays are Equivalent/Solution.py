class StringArrayIterator:
    def __init__(self, arr: List[str]):
        self.arr = arr
        self.ind = 0
        self.word_ind = 0

    def next(self) -> str:
        ret = self.arr[self.ind][self.word_ind]

        if self.word_ind == len(self.arr[self.ind]):
            self.ind += 1
            self.word_ind = 0
        else:
            self.word_ind += 1

        return ret

    def has_next(self) -> bool:
        if self.ind >= len(self.arr):
            return False

        if self.word_ind < len(self.arr[self.ind]):
            return True

        self.ind += 1
        self.word_ind = 0
        return self.has_next()


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        it1, it2 = StringArrayIterator(word1), StringArrayIterator(word2)

        while it1.has_next() and it2.has_next():
            # print(it1.next(), it2.next())
            if it1.next() != it2.next():
                return False


        return not (it1.has_next() or it2.has_next())
