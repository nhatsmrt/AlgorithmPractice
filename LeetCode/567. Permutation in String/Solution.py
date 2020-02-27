class MagnitudeSet:
    def __init__(self, s: str):
        self.cnt = {}
        self.magnitude = 0

        for char in s:
            self.add(char)

    def add(self, char: str):
        prev_cnt = self.cnt.get(char, 0)
        self.magnitude += (prev_cnt + 1) ** 2 - prev_cnt ** 2
        self.cnt[char] = prev_cnt + 1

    def remove(self, char: str):
        prev_cnt = self.cnt.get(char, 0)
        self.magnitude += (prev_cnt - 1) ** 2 - prev_cnt ** 2
        self.cnt[char] = prev_cnt - 1

    def is_empty(self) -> bool:
        return self.magnitude == 0


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        mag_set = MagnitudeSet(s1)
        for i in range(len(s1)):
            mag_set.remove(s2[i])

        if mag_set.is_empty():
            return True

        for i in range(len(s1), len(s2)):
            mag_set.add(s2[i - len(s1)])
            mag_set.remove(s2[i])

            if mag_set.is_empty():
                return True
        return False
