class RollingHash:
    def __init__(self, mod: int=1000000009, p: int=31):
        self.mod, self.p = mod, p
        self.hash_val = 0

    def append(self, char: str):
        value = ord(char) - ord('a') + 1

        self.hash_val = ((self.hash_val * self.p) % self.mod + value) % self.mod


class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        # Time and Space Complexity: O(NL) (on average)
        # O(1) hash collision on average

        prefixes = [({}, {}) for _ in range(len(dict[0]))]
        suffixes = [({}, {}) for _ in range(len(dict[0]))]

        for i, string in enumerate(dict):
            prefix_hash = RollingHash()

            for l, char in enumerate(string):
                prefix_hash.append(char)
                hash_val = prefix_hash.hash_val

                if hash_val not in prefixes[l][0]:
                    prefixes[l][0][hash_val] = set()

                prefixes[l][0][hash_val].add(i)
                prefixes[l][1][i] = hash_val

            suffix_hash = RollingHash()

            for l in range(len(string) - 1, -1, -1):
                char = string[l]
                suffix_hash.append(char)
                hash_val = suffix_hash.hash_val

                if hash_val not in suffixes[l][0]:
                    suffixes[l][0][hash_val] = set()

                suffixes[l][0][hash_val].add(i)
                suffixes[l][1][i] = hash_val

        for i, string in enumerate(dict):
            # differ by first character:
            suffix_hash = suffixes[1][1][i]

            for candidate_ind in suffixes[1][0][suffix_hash]:
                if candidate_ind != i and dict[i][1:] == dict[candidate_ind][1:]:
                    return True

            for l in range(len(string) - 1):
                prefix_hash = prefixes[l][1][i]

                for candidate_ind in prefixes[l][0][prefix_hash]:
                    if candidate_ind != i:
                        if l < len(string) - 2:
                            suffix_hash = suffixes[l + 2][1][i]

                            if candidate_ind in suffixes[l + 2][0][suffix_hash] and dict[i][:l + 1] == dict[candidate_ind][:l + 1] and dict[i][l + 2:] == dict[candidate_ind][l + 2:]:
                                return True
                        elif dict[i][:l + 1] == dict[candidate_ind][:l + 1]:
                            return True


        return False
