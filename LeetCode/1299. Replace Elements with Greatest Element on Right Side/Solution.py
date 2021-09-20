class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Time and Space Complexity: O(N)
        ret = []

        greatest = -1
        for num in reversed(arr):
            ret.append(greatest)
            greatest = max(greatest, num)

        return ret[::-1]
