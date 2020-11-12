class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter()
        for num in nums:
            counter[num] += 1

        ret = []
        self.backtrack([], ret, counter)
        return ret

    def backtrack(self, partial: List[int], ret: List[List[int]], counter):
        choices = list(counter)

        if not choices:
            ret.append(copy.deepcopy(partial))
        else:
            for choice in choices:
                counter[choice] -= 1

                if not counter[choice]:
                    counter.pop(choice)
                partial.append(choice)
                self.backtrack(partial, ret, counter)
                counter[choice] += 1
                partial.pop()
