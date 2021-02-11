class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        largest = -1
        secondLargest = -1

        for num in nums:
            if num >= largest:
                secondLargest = largest
                largest = num
            elif num > secondLargest:
                secondLargest = num

        return (largest - 1) * (secondLargest - 1)
