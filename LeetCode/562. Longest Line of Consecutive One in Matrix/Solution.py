class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        # Time and Space Complexity: O(MN)

        self.dp = {}
        self.step = {
            0: (1, 0), # going down
            1: (0, 1), # going to the right
            2: (1, 1), # diagonal
            3: (1, -1) # anti-diagonal
        }

        ret = 0
        for i in range(len(M)):
            for j in range(len(M[0])):
                for k in range(4):
                    ret = max(ret, self.longest(M, i, j, k))

        return ret

    def longest(self, M, i, j, direction) -> int:
        if (i, j, direction) in self.dp:
            return self.dp[(i, j, direction)]

        if M[i][j] == 0:
            ret = 0
        else:
            ret = 1
            new_i, new_j = i + self.step[direction][0], j + self.step[direction][1]

            if self.is_valid(M, new_i, new_j):
                ret += self.longest(M, new_i, new_j, direction)

        self.dp[(i, j, direction)] = ret
        return ret

    def is_valid(self, M, x, y):
        return x >= 0 and x < len(M) and y >= 0 and y < len(M[0])
