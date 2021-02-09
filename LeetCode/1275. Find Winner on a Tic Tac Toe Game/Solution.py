class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        table = [[0 for j in range(3)] for i in range(3)]

        for i, move in enumerate(moves):
            table[move[0]][move[1]] = i % 2 + 1


        # check rows:
        for row in table:
            if row[0] == row[1] and row[1] == row[2]:
                if row[0] == 1:
                    return "A"
                elif row[0] == 2:
                    return "B"

        # check columns:
        for i in range(3):
            if table[0][i] == table[1][i] and table[1][i] == table[2][i]:
                if table[0][i] == 1:
                    return "A"
                elif table[0][i] == 2:
                    return "B"

        if table[0][0] == table[1][1] and table[1][1] == table[2][2]:
            if table[0][0] == 1:
                return "A"
            elif table[0][0] == 2:
                return "B"

        if table[0][2] == table[1][1] and table[1][1] == table[2][0]:
            if table[0][2] == 1:
                return "A"
            elif table[0][2] == 2:
                return "B"

        if len(moves) == 9:
            return "Draw"

        return "Pending"
