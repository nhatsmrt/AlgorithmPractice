class Solution:
    def minInsertions(self, s: str) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(N)

        rle = []

        start = 0
        end = 0

        while start < len(s):
            if end + 1 < len(s) and s[start] == s[end + 1]:
                end += 1
            else:
                rle.append((s[start], end - start + 1))
                start = end + 1
                end += 1


        ret = 0
        if rle[0][0] == ")":
            open_paren_needed = math.ceil(rle[0][1] / 2)
            close_paren_needed = open_paren_needed * 2
            ret += close_paren_needed - rle[0][1] + open_paren_needed

            start = 1
        else:
            start = 0

        num_opening = 0
        for i in range(start, len(rle), 2):
            open_paren = rle[i][1]
            num_opening += open_paren

            if i == len(rle) - 1:
                close_paren = 0
            else:
                close_paren = rle[i + 1][1]

            if close_paren % 2 == 1:
                close_paren += 1
                ret += 1

            open_paren_needed = close_paren // 2
            ret += max(open_paren_needed - num_opening, 0)
            num_opening = max(num_opening - open_paren_needed, 0)


        return ret + num_opening * 2
