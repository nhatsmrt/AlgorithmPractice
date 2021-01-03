class Solution:
    def countArrangement(self, N: int) -> int:
        return self.count_solutions(set(i for i in range(1, N + 1)))

    def count_solutions(self, remaining: set) -> int:
        if remaining:
            choices = list(remaining)
            index = len(remaining)

            ret = 0

            for choice in choices:
                if not (index % choice) or not (choice % index):
                    remaining.remove(choice)
                    ret += self.count_solutions(remaining)
                    remaining.add(choice)

            return ret
        else:
            return 1
