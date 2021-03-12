class RollingHash:
    _POWER = 2
    _MOD = 1000000007

    def __init__(self, init_str):
        self.data = deque()
        self.hash = 0
        self.last_power = 1

        for char in init_str:
            self.data.append(char)
            self.hash *= self._POWER
            self.hash += self.get_val(char)
            self.hash %= self._MOD

        for _ in range(len(init_str) - 1):
            self.last_power *= self._POWER

    def get_val(self, char: str) -> int:
        return ord(char) - ord('0') + 1

    def insert(self, char: str):
        removed = self.data.popleft()
        self.data.append(char)

        self.hash -= self.last_power * self.get_val(removed)
        self.hash *= self._POWER
        self.hash += self.get_val(char)
        self.hash %= self._MOD


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Time and Space Complexity: O(N + K) (w.h.p)

        binary_str = {}
        rolling_hash = RollingHash(s[:k])
        binary_str[rolling_hash.hash] = [0]

        for i in range(k, len(s)):
            rolling_hash.insert(s[i])
            substr_start = i - k + 1
            if rolling_hash.hash not in binary_str:
                binary_str[rolling_hash.hash] = [substr_start]
            else:
                binary_str[rolling_hash.hash].append(substr_start)

        if len(binary_str) == 2 ** k:
            return True

        ret = 0
        for hash_val in binary_str:
            start_inds = binary_str[hash_val]
            if len(start_inds) == 1:
                ret += 1
            else:
                ret += len(set(map(lambda ind: s[ind:ind + k], start_inds)))

        return ret == 2 ** k
