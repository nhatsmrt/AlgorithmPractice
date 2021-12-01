class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # Idea 1: there is a k-repeat m-pattern when arr[i] == arr[i + m] for m(k - 1) times consecutively
        # Idea 2: Keep track of the cnt of shifted equality so far. If arr[i] != arr[i + m], we can clear this count, since no k-repeat m-pattern can contain i + m.

        cnt = 0
        for start in range(len(arr) - m):
            shifted_start = start + m

            if arr[start] == arr[shifted_start]:
                cnt += 1
            else:
                cnt = 0

            if cnt == m * (k - 1):
                return True

        return False
