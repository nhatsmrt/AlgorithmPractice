class Solution:
    def countSubstrings(self, s: str) -> int:
        # Modified Manacher's algorithm
        # Time and Space Complexity: O(N)

        s_arr = ["%", "#"]
        for i in range(len(s)):
            s_arr.append(s[i])
            s_arr.append("#")
        s_arr.append("^")
        # append weird characters to avoid bound checking

        lengths = [0, 0]
        cur_cent = 1
        cur_right = 1

        for i in range(2, len(s_arr) - 2):
            mirror = 2 * cur_cent - i

            length = min(cur_right - i, lengths[mirror]) if i < cur_right else 0
            while s_arr[i + length + 1] == s_arr[i - length - 1]:
                length += 1

            if i + length > cur_right:
                cur_right = i + length
                cur_cent = i
            lengths.append(length)

        return sum(map(lambda x: (x + 1) // 2, lengths))
        
