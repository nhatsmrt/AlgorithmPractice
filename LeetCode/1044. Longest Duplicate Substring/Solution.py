class Solution:
    def longestDupSubstring(self, S: str) -> str:
        self.p = 26
        self.m = 999983

        low = 0
        high = len(S)
        ret = None

        self.prehash = [0] * len(S)
        self.prehash[0] = (ord(S[0]) - ord('a') + 1)
        power = self.p

        for i in range(1, len(S)):
            self.prehash[i] = (self.prehash[i - 1] + ((ord(S[i]) - ord('a') + 1) * power) % self.m) % self.m
            power = (power * self.p) % self.m

        while low <= high:
            mid = high - (high - low) // 2
            candidate = self.findDup(S, mid)

            if candidate != None:
                ret = candidate
                low = mid + 1
            else:
                high = mid - 1

        return ret if ret is not None else ""

    def findDup(self, S: str, length: int) -> str:
        substrings = {}
        power = 1

        for i in range(len(S) - 1, length - 2, -1):
            hash = self.prehash[i]
            if i > length - 1:
                hash = (hash + self.m - self.prehash[i - length]) % self.m

            hash *= power
            hash %= self.m

            substr = S[i - length + 1:i + 1]
            if not hash in substrings:
                substrings[hash] = {i}
            else:
                for end in substrings[hash]:
                    if S[end - length + 1:end + 1] == substr:
                        return substr
                substrings[hash].add(i)

            power *= self.p
            power %= self.m

        return None
