class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one = -1

        for i, num in enumerate(nums):
            if num == 1:
                if last_one >= 0 and i - last_one <= k:
                    return False

                last_one = i

        return True
