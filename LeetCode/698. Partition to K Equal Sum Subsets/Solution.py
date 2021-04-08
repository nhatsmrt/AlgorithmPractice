class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Time Complexity: O(N * 2^N * target)
        # Space Complexity: O(target * 2^N)
        # where target = sum(nums) / k

        total_sum = sum(nums)

        if total_sum % k:
            return False

        target = total_sum // k
        self.dp = {}
        return self.solve(nums, 0, set(range(len(nums))), target, 0)

    def solve(self, nums: List[int], mask: int, unused: set, target: int, cur_group_sum: int):
        if (mask, cur_group_sum) in self.dp:
            return self.dp[(mask, cur_group_sum)]

        if not unused:
            ret = (cur_group_sum % target) == 0
        else:
            ret = False
            for i in unused:
                num = nums[i]

                if cur_group_sum + num <=  target:
                    unused.remove(i)

                    new_mask = mask | (1 << i)
                    ret = ret or self.solve(nums, new_mask, unused, target, (cur_group_sum + num) % target)

                    unused.add(i)

        self.dp[(mask, cur_group_sum)] = ret
        return ret
        
