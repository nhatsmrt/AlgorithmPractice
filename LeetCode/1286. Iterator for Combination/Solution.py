class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        # Time and Space Complexity: O(combinationLength)

        self.characters, self.combinationLength = characters, combinationLength
        self.used = False
        self.inds = [i for i in range(combinationLength)]

    def next(self) -> str:
        # Time Complexity: O(combinationLength)

        if self.used:
            self.increment(self.inds)
        self.used = True
        return ''.join(list(map(lambda ind: self.characters[ind], self.inds)))

    def hasNext(self) -> bool:
        # Time Complexity: O(combinationLength)
        return self.increment(self.inds)

    def increment(self, inds: List[int]) -> bool:
        if not self.used:
            return True

        for i in range(len(inds) - 1, -1, -1):
            if len(inds) - i + self.inds[i] != len(self.characters):
                inds[i] += 1
                for j in range(i + 1, len(inds)):
                    inds[j] = inds[j - 1] + 1

                self.used = False
                return True
        return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
