class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # Time and Space Complexity: O(sum(len(string)))

        def shift_seq(string):
            ret = []

            for i in range(1, len(string)):
                ret.append((ord(string[i]) - ord(string[i - 1]) + 26) % 26)

            return tuple(ret)

        ret = []

        groups = {}
        for string in strings:
            key = shift_seq(string)

            if key not in groups:
                groups[key] = []

            groups[key].append(string)

        return [groups[key] for key in groups]
