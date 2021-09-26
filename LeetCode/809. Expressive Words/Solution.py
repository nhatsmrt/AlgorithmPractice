def condense(string):
    ret = []

    start = 0
    end = 0

    while start < len(string):
        if end + 1 < len(string) and string[end + 1] == string[start]:
            end += 1
        else:
            ret.append((string[start], end - start + 1))
            start = end + 1
            end = start

    return ret

def check(group1, group2):
    return group1[0] == group2[0] and (group1[1] == group2[1] or (group1[1] > group2[1] and group1[1] >= 3))

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        # Time and Space Complexity: O(|s| + sum(|word| for word in words))

        condensed_s = condense(s)

        ret = 0
        for word in map(condense, words):
            if len(word) == len(condensed_s) and all(starmap(check, zip(condensed_s, word))):
                ret += 1

        return ret
