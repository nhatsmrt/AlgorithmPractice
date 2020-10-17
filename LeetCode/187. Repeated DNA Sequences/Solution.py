class RollingHash:
    def __init__(self, mod):
        self.value = {
            "A": 1, "C": 2, "G": 3, "T": 4
        }
        self.hash = 0
        self.MOD = mod


        self.first_power = 1
        for _ in range(9):
            self.first_power = self.first_power * 4
            self.first_power %= self.MOD

    def add(self, char: str):
        self.hash = (self.hash * 4 + self.value[char]) % self.MOD

    def remove(self, char: str):
        self.hash -= self.value[char] * self.first_power
        self.hash %= self.MOD

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []

        rolling = RollingHash(1001)
        for i in range(10):
            rolling.add(s[i])

        substrings = {rolling.hash: [0]}
        ret = set()

        for i in range(10, len(s)):
            rolling.remove(s[i - 10])
            rolling.add(s[i])
            start = i - 10 + 1

            if rolling.hash in substrings:
                for candidate in substrings[rolling.hash]:
                    if s[candidate:candidate + 10] == s[start:start + 10]:
                        if candidate not in ret:
                            ret.add(candidate)

                        break
            else:
                substrings[rolling.hash] = []

            substrings[rolling.hash].append(start)

        return list(map(lambda start: s[start:start + 10], ret))
