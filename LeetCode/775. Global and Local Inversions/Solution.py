class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        cumsum = 0
        target = 0

        for i, num in enumerate(A):
            cumsum += num
            target += i

            if abs(cumsum - target) > 1:
                return False

        return True
