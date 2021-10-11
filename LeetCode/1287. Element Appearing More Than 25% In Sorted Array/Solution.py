class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        start = 0
        end = 0

        while start < len(arr):
            if end + 1 < len(arr) and arr[end + 1] == arr[start]:
                end += 1
            else:
                cnt = end - start + 1

                if cnt > 0.25 * len(arr):
                    return arr[start]

                start = end + 1
                end += 1
