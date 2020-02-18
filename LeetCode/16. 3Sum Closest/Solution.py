class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret = 1000000000

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                candidate = nums[i] + nums[j] + nums[k]
                if abs(candidate - target) < abs(ret - target):
                    ret = candidate

                if candidate == target:
                    return candidate

                if candidate < target:
                    j += 1
                else:
                    k -= 1

        return ret
