class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # Time and Space Complexity: O(N)

        by_size = {}
        ret = []

        for i, size in enumerate(groupSizes):
            if size not in by_size:
                by_size[size] = []

            by_size[size].append(i)

        for size in range(max(groupSizes) + 1):
            if size in by_size:
                for j in range(0, len(by_size[size]), size):
                    ret.append(by_size[size][j:j + size])


        return ret
