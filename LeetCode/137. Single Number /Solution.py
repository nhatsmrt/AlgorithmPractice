class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = dup = 0

        for num in nums:
            # If a number appears once, it will stay in unique
            # If a number appears three time: it will be added to unique
            # then remove from unique and add to dup (2nd appearance)
            # then doesn't get added to unique in the third appearance

            unique = ~dup & (unique ^ num)
            dup = ~unique & (dup ^ num)

        return unique
        
