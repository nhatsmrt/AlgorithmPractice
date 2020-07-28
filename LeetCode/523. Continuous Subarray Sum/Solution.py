class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k < 0:
            return self.checkSubarraySum(nums, -k)

        if k == 0:
            for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True

            return False

        # pigeonhole principle
        if len(nums) > 2 * k:
            return True

        mods = {nums[0] % k: [0]}

        for i in range(1, len(nums)):
            nums[i] = (nums[i] + nums[i - 1]) % k

            if nums[i] == 0:
                return True

            if nums[i] in mods and (len(mods[nums[i]]) > 1 or mods[nums[i]][0] != i - 1):
                return True
            elif nums[i] not in mods:
                mods[nums[i]] = []

            mods[nums[i]].append(i)

        return False
