class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Time Complexity: O(2^N)
        # Space Complexity: O(N)

        arr = list(filter(lambda string: len(string) == len(set(string)), arr))
        return self.build(arr, [0] * 26, 0)

    def build(self, arr: List[str], mask: List[int], i: int) -> int:
        if i == len(arr):
            return sum(mask)

        ret = self.build(arr, mask, i + 1)

        for char in arr[i]:
            if mask[self.getInd(char)]:
                return ret

        for char in arr[i]:
            mask[self.getInd(char)] = 1

        ret = max(ret, self.build(arr, mask, i + 1))

        for char in arr[i]:
            mask[self.getInd(char)] = 0

        return ret

    def getInd(self, char: str) -> int:
        return ord(char) - ord('a')
