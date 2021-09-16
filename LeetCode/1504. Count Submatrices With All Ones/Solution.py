class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # Time and Space Complexity: O(MN)

        zeros_up = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]

        for j in range(len(mat[0])):
            cum = 0
            for i in range(len(mat)):
                cum = cum * mat[i][j] + mat[i][j]
                zeros_up[i][j] = cum


        ret = 0
        for i in range(len(mat)):
            stack = []
            stack_size = 0

            for j in range(len(mat[0])):
                cnt = 1

                while stack and zeros_up[i][j] <= stack[-1][0]:
                    top, top_cnt, _ = stack.pop()
                    cnt += top_cnt

                cum_sum = cnt * zeros_up[i][j]
                if stack:
                    cum_sum += stack[-1][-1]

                ret += cum_sum

                stack.append((zeros_up[i][j], cnt, cum_sum))


        return ret
