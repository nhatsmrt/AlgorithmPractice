class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ret = []
        start = 0
        end = 0

        while start < len(s):
            if end + 1 < len(s) and s[end + 1] == s[start]:
                end += 1
            else:
                if end - start + 1 >= 3:
                    ret.append([start, end])

                end += 1
                start = end

        return ret
