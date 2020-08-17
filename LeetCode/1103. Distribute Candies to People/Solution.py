class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # Time and Space Complexity: O(N)

        num_rounds = self.find_num_round(candies)
        ret = [0] * num_people

        # each person get num_rounds // num_people full rounds:
        num_full_rounds = num_rounds // num_people
        for i in range(num_people):
            ret[i] += num_full_rounds * ((i + 1) + (i + 1) + (num_full_rounds - 1) * num_people) // 2

        # last finished rounds:
        start = num_full_rounds * num_people
        remaining = candies - start * (start + 1) // 2

        for i in range(num_rounds % num_people):
            if remaining > start + i + 1:
                ret[i] += start + i + 1
                remaining -= start + i + 1
            else:
                ret[i] += remaining
                remaining = 0

        if remaining > 0:
            # last, unfinished round:
            i = (i + 1) % num_people
            ret[i] += remaining
        return ret

    def find_num_round(self, candies: int):
        return int(math.sqrt(2 * candies + 0.25) - 0.5)
