class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Time and Space Complexity: O(N)

        prefix = [0] + list(accumulate(nums))
        cnter = []

        for pre_sum in prefix:
            if pre_sum == len(cnter):
                cnter.append(0)

            cnter[-1] += 1


        ret = 0
        for fst in range(len(cnter)):
            snd = fst + goal

            if snd < len(cnter):
                if fst == snd:
                    ret += cnter[fst] * (cnter[fst] - 1) // 2
                else:
                    ret += cnter[fst] * cnter[snd]

        return ret
