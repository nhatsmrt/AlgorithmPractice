class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # Time and Space Complexity: O(N)

        stack = []

        for i, num in enumerate(nums):
            poppable = (len(nums) - i + len(stack)) - k

            while stack and poppable > 0 and stack[-1] > num:
                stack.pop()
                poppable -= 1

            stack.append(num)

        return stack[:k]
