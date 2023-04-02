class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens = sorted(nums[i] for i in range(0, len(nums), 2))
        odds = sorted([nums[i] for i in range(1, len(nums), 2)], reverse=True)
        ret = []

        for i in range(len(nums)):
            if i % 2 == 0:
                ret.append(evens[i // 2])
            else:
                ret.append(odds[i // 2])

        return ret
