class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # Time and Space Complexity: O(N)

        ret = []

        cur_max = -1
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > cur_max:
                ret.append(i)

            cur_max = max(cur_max, heights[i])

        return ret[::-1]
