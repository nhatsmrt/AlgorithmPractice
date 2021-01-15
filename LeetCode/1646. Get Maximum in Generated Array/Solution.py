class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # Time and Space Complexity: O(N)

        if n <= 1:
            return n

        arr = [0, 1]

        for i in range(2, n + 1):
            if i % 2:
                arr.append(arr[i // 2] + arr[i // 2 + 1])
            else:
                arr.append(arr[i // 2])

        return max(arr)
