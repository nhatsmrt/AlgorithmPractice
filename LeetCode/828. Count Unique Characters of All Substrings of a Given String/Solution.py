class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # Time and Space Complexity: O(|s|)

        index = {}

        for i, char in enumerate(s):
            if char not in index:
                index[char] = []

            index[char].append(i)

        ret = 0
        for _, occ in index.items():
            start = 0

            for i in range(0, len(occ) - 1):
                end = occ[i + 1] - 1
                ret += (occ[i] - start + 1) * (end - occ[i] + 1)
                start = occ[i] + 1

            ret += (occ[-1] - start + 1) * (len(s) - occ[-1])

        return ret
