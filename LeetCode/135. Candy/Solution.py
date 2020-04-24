class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Time and Space Complexity: O(n)

        heights_left = [0] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                heights_left[i] = heights_left[i - 1] + 1
            else:
                heights_left[i] = 0

        heights_right = [0] * len(ratings)
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                heights_right[i] = heights_right[i + 1] + 1
            else:
                heights_right[i] = 0


        ret = 0
        for i in range(len(heights_left)):
            ret += max(heights_left[i], heights_right[i]) + 1
        return ret
