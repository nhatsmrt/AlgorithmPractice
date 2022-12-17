class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Time Compleixty: O(N)
        # Space Complexity: O(1)

        top_3 = [None] * 3

        for num in nums:
            if top_3[0] is None or num > top_3[0]:
                top_3 = [num] + top_3[:2]
            elif top_3[0] is not None and top_3[0] > num and (top_3[1] is None or num > top_3[1]):
                top_3 = [top_3[0], num] + [top_3[1]]
            elif top_3[1] is not None and top_3[1] > num and (top_3[2] is None or num > top_3[2]):
                top_3 = top_3[:2] + [num]

        return top_3[-1] if top_3[-1] is not None else top_3[0]
