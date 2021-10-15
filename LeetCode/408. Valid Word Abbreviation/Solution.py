class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        i = 0
        j = 0

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == "0": # leading zero
                    return False

                start = j
                end = j

                while end + 1 < len(abbr) and abbr[end + 1].isdigit():
                    end += 1

                cnt = int(abbr[start:end + 1])
                j = end + 1
                i += cnt
            else:
                if word[i] != abbr[j]: # not match
                    return False

                i += 1
                j += 1

        return i == len(word) and j == len(abbr)
