class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # Time Complexity: O(MN + range)
        # Space Complexity: O(MN)

        index = {}
        min_val = 1000000000
        max_val = -1000000000

        for i, row in enumerate(mat):
            for val in row:
                if val not in index:
                    index[val] = set()

                index[val].add(i)
                min_val = min(val, min_val)
                max_val = max(val, max_val)

        for val in range(min_val, max_val + 1):
            if len(index.get(val, [])) == len(mat):
                return val

        return -1
