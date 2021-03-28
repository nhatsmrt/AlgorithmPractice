class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Time and Space Complexity: O(N)

        # Find the longest palindrome containing the start of the string
        # This can be done via Manacher's algorithm

        s_arr = ["<start>", "$"]

        for char in s:
            s_arr.append(char)
            s_arr.append("$")

        s_arr.append("<end>")


        # palin[i] is the length of longest palindrome centered at i
        palin = [1] * len(s_arr)
        cur_left = 0
        cur_right = -1


        for center in range(1, len(s_arr) - 1):
            if center > cur_right: # outside of longest palindrome
                delta = 0
            else:
                mirror = cur_left + (cur_right - center)
                delta = min(cur_right - center, palin[mirror] // 2)

            while s_arr[center + delta + 1] == s_arr[center - delta - 1]:
                delta += 1

            cur_right = center + delta
            cur_left = center - delta
            palin[center] = 2 * delta + 1

        best_length = 0
        best_center = -1

        for center in range(1, len(s_arr) - 1):
            delta = palin[center] // 2
            left_boundary = center - delta

            if left_boundary < 2:
                if delta > best_length:
                    best_length = delta
                    best_center = center


        ret = []
        for i in range(len(s) - 1, best_length - 1, -1):
            ret.append(s[i])

        for char in s:
            ret.append(char)

        return "".join(ret)
