class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        self.num_divisible = [-1] * len(nums)
        self.next = [-1] * len(nums)

        argmax = 0
        curmax = 0

        for i in range(len(nums)):
            if self.largest_from(nums, i) > curmax:
                argmax = i
                curmax = self.largest_from(nums, i)

        ret = []
        for i in range(curmax):
            ret.append(nums[argmax])
            argmax = self.next[argmax]

        return ret

    def largest_from(self, nums: List[int], i: int) -> int:
        if self.num_divisible[i] > -1:
            return self.num_divisible[i]

        curmax = 1
        argmax = i

        for cand_ind in range(i + 1, len(nums)):
            if nums[cand_ind] % nums[i] == 0:
                candidate = 1 + self.largest_from(nums, cand_ind)

                if candidate > curmax:
                    curmax = candidate
                    argmax = cand_ind

        self.num_divisible[i] = curmax
        self.next[i] = argmax

        return curmax
        
