class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        # Time and Space Complexity: O(N)
        # (each number enters the ret once
        # and exit ret at most once)

        ret = [0]
        next_max = 1
        i = 0

        while i < len(S):
            if S[i] == "I":
                ret.append(next_max)
                next_max += 1
                i += 1
            else:
                j = i
                while j < len(S) and S[j] == "D":
                    j += 1

                # S[i], ..., S[j + 1] is D
                old_peak = ret.pop()
                new_peak = old_peak + j - i
                ret.append(new_peak)

                for val in range(new_peak - 1, old_peak - 1, -1):
                    ret.append(val)

                next_max = new_peak + 1
                i = j

        return ret
