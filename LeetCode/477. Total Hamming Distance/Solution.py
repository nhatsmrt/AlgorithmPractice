class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # Time Complexity: O(NW) = O(N log MAX)
        # Space Complexity: O(N)

        one_cnter = []

        for num in nums:
            i = 0
            while num > 0:
                if num % 2 == 1:
                    if i == len(one_cnter):
                        one_cnter.append(1)
                    else:
                        one_cnter[i] += 1
                elif i == len(one_cnter):
                    one_cnter.append(0)


                i += 1
                num //= 2

        return sum(map(lambda cnt: cnt * (len(nums) - cnt), one_cnter))
