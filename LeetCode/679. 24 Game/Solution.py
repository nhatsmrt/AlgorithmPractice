class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        # Time and Space Complexity: O(1)
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-4

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                remaining = [nums[k] for k in range(len(nums)) if k != i and k != j]

                candidates = [
                    nums[i] + nums[j],
                    nums[i] * nums[j],
                    nums[i] - nums[j],
                    nums[j] - nums[i]
                ]

                if nums[j]:
                    candidates.append(nums[i] / nums[j])

                if nums[i]:
                    candidates.append(nums[j] / nums[i])

                for candidate in candidates:
                    remaining.append(candidate)
                    if self.judgePoint24(remaining):
                        return True

                    remaining.pop()

        return False
