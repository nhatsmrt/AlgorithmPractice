def find_max_point(cur_val, cnter, solutions):
    if cur_val <= 1:
        return cnter[cur_val]

    if solutions[cur_val - 1] is not None:
        return solutions[cur_val - 1]

    solutions[cur_val - 1] = max(
        find_max_point(cur_val - 1, cnter, solutions),
        find_max_point(cur_val - 2, cnter, solutions) + cnter[cur_val] * cur_val,
    )

    return solutions[cur_val - 1]



class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Time and Space Complexity: O(N + max_val)
        cnter = Counter(nums)
        max_val = max(nums)

        return find_max_point(max_val, cnter, [None] * max_val)
