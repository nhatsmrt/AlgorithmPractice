class Solution:
    def modifyString(self, s: str) -> str:
        # Time and Space Complexity: O(N)
        last = "$"

        ret = []
        for i, char in enumerate(s):
            if char == "?":
                forbidden = [last]

                if i + 1 < len(s):
                    forbidden.append(s[i + 1])

                for char_ind in range(26):
                    cand = chr(ord('a') + char_ind)

                    if cand not in forbidden:
                        last = cand
                        ret.append(cand)
                        break
            else:
                last = char
                ret.append(char)

        return "".join(ret)
