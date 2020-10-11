def to_ind(char):
    return ord(char) - ord('a')

def to_char(ind):
    return chr(ind + ord('a'))

def is_valid(occs, chars_required, require):
    satisfied = 0
    for char in chars_required:
        if occs[to_ind(char)] != -1:
            satisfied += 1

    return satisfied == require

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Time and Space Complexity: O(N)

        chars_used = set(iter(s))
        next_occ = [[-1] * 26 for _ in range(len(s))]
        next_occ[-1][to_ind(s[-1])] = len(s) - 1

        for i in range(len(s) - 2, -1, -1):
            next_occ[i] = copy.deepcopy(next_occ[i + 1])
            next_occ[i][to_ind(s[i])] = i

        ret = []

        cur_str_index = 0
        while chars_used:
            next_char = ""
            next_str_ind = -1

            for char in chars_used:
                candidate_str_ind = next_occ[cur_str_index][to_ind(char)]
                if is_valid(next_occ[candidate_str_ind], chars_used, len(chars_used)) and (not next_char or next_char > char):
                    next_char = char
                    next_str_ind = candidate_str_ind


            ret.append(next_char)
            cur_str_index = next_str_ind + 1
            chars_used.remove(next_char)

        return "".join(ret)
