from typing import Tuple


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Time and Space Complexity: O(N 2^N)
        # Extra space: O(N)
        nums.sort()

        consolidated_nums = []
        for num in nums:
            if not consolidated_nums:
                consolidated_nums.append((num, 1))
            else:
                lst, lst_cnt = consolidated_nums.pop()

                if lst == num:
                    consolidated_nums.append((num, lst_cnt + 1))
                else:
                    consolidated_nums.extend([(lst, lst_cnt), (num, 1)])

        all_sols = []
        self.build(consolidated_nums, 0, 0, [], all_sols)
        return all_sols

    def build(self, nums: List[Tuple[int, int]], i: int, used: int, partial: List[int], all_sols: List[List[int]]):
        if i == len(nums):
            all_sols.append(copy.copy(partial))
        else:
            self.build(nums, i + 1, 0, partial, all_sols)

            if used < nums[i][1]:
                partial.append(nums[i][0])
                self.build(nums, i, used + 1, partial, all_sols)
                partial.pop()
