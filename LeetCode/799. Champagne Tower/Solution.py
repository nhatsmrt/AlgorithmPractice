class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cur_row = [poured]

        for r in range(query_row):
            next_row = [0] * (len(cur_row) + 1)


            for i in range(len(cur_row)):
                if cur_row[i] > 1.0:
                    amount_added_next_row = (cur_row[i] - 1.0) / 2
                    next_row[i] += amount_added_next_row
                    next_row[i + 1] += amount_added_next_row

            cur_row = next_row

        if cur_row[query_glass] > 1.0:
            return 1.0
        return cur_row[query_glass]    
