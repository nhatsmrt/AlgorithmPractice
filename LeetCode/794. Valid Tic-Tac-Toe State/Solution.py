class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # Time and Space Complexity: O(1)

        total_cnt = Counter()
        cnters = {}
        cnters['X'] = Counter()
        cnters['O'] = Counter()

        for i in range(3):
            for j in range(3):
                symbol = board[i][j]

                if symbol != ' ':
                    cnter = cnters[symbol]

                    total_cnt[symbol] += 1

                    cnter['row_{}'.format(i)] += 1
                    cnter['col_{}'.format(j)] += 1

                    if i == j: # anti-diagonal:
                        cnter['anti'] += 1

                    if i + j == 2: # main-diagonal
                        cnter['main'] += 1

        if total_cnt['O'] > total_cnt['X']:
            return False # player X plays first so should always have at least as many moves

        if abs(total_cnt['X'] - total_cnt['O']) > 1:
            return False # players take turn

        x_win = [key for key in cnters['X'] if cnters['X'][key] == 3]
        o_win = [key for key in cnters['O'] if cnters['O'][key] == 3]

        if all([x_win, o_win]):
            return False # at most one player can win

        if not any([x_win, o_win]):
            return True # neither win is fine

        if x_win and total_cnt['X'] == total_cnt['O']:
            return False # if x win then x should have one extra move

        if o_win and total_cnt['X'] != total_cnt['O']:
            return False

        win = x_win if x_win else o_win

        if len(win) <= 2:
            return True

        n_row = len([key for key in win if key.startswith('row')])
        n_col = len([key for key in win if key.startswith('col')])

        if n_row >= 2 or n_col >= 2:
            return False

        return True
