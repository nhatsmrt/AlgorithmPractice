DOWN = 0
UP = 1
RIGHT = 2
LEFT = 3

DIRECTIONS = [DOWN, UP, RIGHT, LEFT]

CHECK_CELL = [(-1, 0), (1, 0), (0, -1), (0, 1)]
MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def is_valid(board, i, j):
    return i >= 0 and i < len(board) and j >= 0 and j < len(board[0])

def can_end(board, checked_i, checked_j):
    return not is_valid(board, checked_i, checked_j) or board[checked_i][checked_j] == '#'

def can_start(board, i, j, direction, word):
    if board[i][j] != ' ' and board[i][j] != word[0]:
        return False

    # not enough space:
    if direction == DOWN and i + len(word) > len(board):
        return False
    elif direction == UP and i + 1 < len(word):
        return False
    elif direction == LEFT and j + 1 < len(word):
        return False
    elif direction == RIGHT and j + len(word) > len(board[0]):
        return False

    checked_i, checked_j = i + CHECK_CELL[direction][0], j + CHECK_CELL[direction][1]

    checked_i_2, checked_j_2 = i + MOVES[direction][0] * len(word), j + MOVES[direction][1] * len(word)

    return can_end(board, checked_i, checked_j) and can_end(board, checked_i_2, checked_j_2)

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        # Time Complexity: O(MN)
        # Each cell in board can only be one of the ends, or the middle of the word, but not both
        # Space Complexity: O(1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                for direction in DIRECTIONS:
                    if can_start(board, i, j, direction, word):
                        cur_i, cur_j = i, j

                        for word_ind in range(len(word)):
                            if board[cur_i][cur_j] != " " and board[cur_i][cur_j] != word[word_ind]:
                                break

                            cur_i, cur_j = cur_i + MOVES[direction][0], cur_j + MOVES[direction][1]
                        else:
                            return True

        return False
