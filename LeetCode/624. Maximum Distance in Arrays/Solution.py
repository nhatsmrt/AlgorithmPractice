class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mins = list(map(operator.itemgetter(0), arrays))
        maxes = list(map(operator.itemgetter(-1), arrays))

        smallest, smallest_2 = self.find_two(mins, lambda x, y: x > y)
        largest, largest_2 = self.find_two(maxes, lambda x, y: x < y)


        if smallest[0] != largest[0]:
            return largest[1] - smallest[1]
        else:
            return max(largest[1] - smallest_2[1], largest_2[1] - smallest[1])

    def find_two(self, arr: List[int], condition) -> int:
        first = None
        second = None

        for i, num in enumerate(arr):
            if first is None or condition(first[1], num):
                second = first
                first = i, num
            elif second is None or condition(second[1], num):
                second = i, num

        return first, second
