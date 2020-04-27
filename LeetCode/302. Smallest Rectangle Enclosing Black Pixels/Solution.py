class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        # Time Complexity: O(M log N + N log M)
        # Space Complexity: O(1)

        low = 0
        high = x

        while low < high:
            mid = low + (high - low) // 2

            if sum(int(image[mid][i]) for i in range(len(image[0]))) == 0:
                low = mid + 1
            else:
                high = mid

        row0 = low


        low = x
        high = len(image) - 1

        while low < high:
            mid = high - (high - low) // 2

            if sum(int(image[mid][i]) for i in range(len(image[0]))) == 0:
                high = mid - 1
            else:
                low = mid

        row1 = low


        low = 0
        high = y

        while low < high:
            mid = low + (high - low) // 2

            if sum(int(image[i][mid]) for i in range(len(image))) == 0:
                low = mid + 1
            else:
                high = mid

        col0 = low


        low = y
        high = len(image[0]) - 1

        while low < high:
            mid = high - (high - low) // 2

            if sum(int(image[i][mid]) for i in range(len(image))) == 0:
                high = mid - 1
            else:
                low = mid

        col1 = low

        return (col1 - col0 + 1) * (row1 - row0 + 1)
