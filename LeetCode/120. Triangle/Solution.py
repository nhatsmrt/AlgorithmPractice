class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        cur = [triangle[0][0]]
        for d in range(1, len(triangle)):
            new_level = []
            for i in range(len(triangle[d])):
                if i == 0:
                    new_level.append(cur[0] + triangle[d][i])
                elif i == len(triangle[d]) - 1:
                    new_level.append(cur[len(cur) - 1] + triangle[d][i])
                else:
                    new_level.append(min(cur[i - 1], cur[i]) + triangle[d][i])
            cur = new_level

        return min(cur)
        
