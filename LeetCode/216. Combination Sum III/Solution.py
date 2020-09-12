class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ret = []
        self.build(k, n, [], 0, ret)
        return ret


    def build(self, k: int, n: int, sol: List[int], sol_sum: int, ret: List[List[int]]):
        if len(sol) == k:
            if sol_sum == n:
                ret.append(copy.deepcopy(sol))
        else:
            lower_bound = 1 if not sol else sol[-1] + 1
            upper_bound = min(n - sol_sum + 1, 10)

            for val in range(lower_bound, upper_bound):
                sol.append(val)
                self.build(k, n, sol, sol_sum + val, ret)
                sol.pop()
