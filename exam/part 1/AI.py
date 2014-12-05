# very unfinished and ugly
from random import shuffle


class AI:

    EMPTY_CELL = "*"
    PLAYER_SIGN = "X"
    AI_SIGN = "O"
    PLAYER_WINS = "Congratulations! You win!"
    AI_WINS = "Computer wins!"
    IMPOSSIBLE_MOVE = "You can't play that cell! Try again!"
    USED_CELL = -1

    def __init__(self):
        self.players_board = [[AI.EMPTY_CELL, AI.EMPTY_CELL, AI.EMPTY_CELL],
                              [AI.EMPTY_CELL, AI.EMPTY_CELL, AI.EMPTY_CELL],
                              [AI.EMPTY_CELL, AI.EMPTY_CELL, AI.EMPTY_CELL]]
        self.potential_board = [[3, 2, 3],
                                [2, 4, 2],
                                [3, 2, 3]]
        self.player_critical_cells = []
        self.AI_critical_cells = []

    def make_move(self):
        if self.__does_AI_win():
            return AI.AI_WINS
        if self.__block_player_victory_move() is not False:
            move_to = self.__block_player_victory_move()
        elif self.__block_player_fork_move() is not False:
            move_to = self.__block_player_fork_move()
        else:
            move_to = self.__max_potential_move()

        row = move_to[0]
        col = move_to[1]

        self.__update_players_board(row, col, AI.AI_SIGN)
        self.potential_board[row][col] = AI.USED_CELL
        self.__update_critiacal_cells(AI.AI_SIGN)

    def player_move(self, row, col):
        if self.__check_free(row, col):
            self.__update_players_board(row, col, AI.PLAYER_SIGN)
            if self.__is_victory(row, col):
                return AI.PLAYER_WINS
            self.__update_potential_board(row, col)
            self.__update_critical_cells(AI.PLAYER_SIGN)
        else:
            return AI.IMPOSSIBLE_MOVE

    def __does_AI_win(self):
        if self.AI_critical_cells is not []:
            shuffle(self.AI_critical_cells)
            row = self.AI_critical_cells[0][0]
            col = self.AI_critical_cells[0][1]
            self.__update_players_board(row, col, AI.AI_SIGN)
            return True
        else:
            return False

    def __block_player_victory_move(self):
        if self.player_critical_cells is not []:
            shuffle(self.player_critical_cells)
            row = self.player_critical_cells[0][0]
            col = self.player_critical_cells[0][1]
            self.player_critical_cells.remove((row, col))
            return (row, col)
        else:
            return False

    def __block_player_fork_move(self):
        center_cell = (self.players_board[1][1] == AI.AI_SIGN)
        if center_cell:
            up_left_cell = (self.players_board[0][0] == AI.PLAYER_SIGN)
            down_right_cell = (self.players_board[2][2] == AI.PLAYER_SIGN)
            major_diagonal_occupied = (up_left_cell and down_right_cell)

            up_right_cell = (self.players_board[0][2] == AI.PLAYER_SIGN)
            down_left_cell = (self.players_board[2][0] == AI.PLAYER_SIGN)
            minor_diagonal_occupied = (up_right_cell and down_left_cell)

            if major_diagonal_occupied and minor_diagonal_occupied:
                move_to = self.__find_appropriate_field()
                return move_to
        else:
            return False

    def __find_appropriate_field(self):
        potential_cells = [(0, 1), (1, 0), (1, 2), (2, 1)]
        empty_cells = list(filter(lambda x: self.potential_board[x[0]][x[1]] !=
                                  AI.USED_CELL, potential_cells))
        shuffle(empty_cells)
        if len(empty_cells) != 0:
            return empty_cells[0]
        return False

    def __max_potential_move(self):
        max_potential = max(list(map(lambda x: max(x), self.potential_board)))
        potential_cells = []
        for row in range(3):
            for col in range(3):
                if self.potential_board[row][col] == max_potential:
                    potential_cells.append((row, col))
        shuffle(potential_cells)
        return potential_cells[0]

    def __update_critical_cells(self, kind_of_player):
        new_critical_cells = []

        row1 = [(0, 0), (0, 1), (0, 2)]
        row2 = [(1, 0), (1, 1), (1, 2)]
        row3 = [(2, 0), (2, 1), (2, 2)]

        col1 = [(0, 0), (1, 0), (2, 0)]
        col2 = [(0, 1), (1, 1), (2, 1)]
        col3 = [(0, 2), (1, 2), (2, 2)]

        major_diagonal = [(0, 0), (1, 1), (2, 2)]
        minor_diagonal = [(0, 2), (1, 1), (2, 0)]

        triples_to_check = [row1, row2, row3, col1, col2, col3,
                            major_diagonal, minor_diagonal]

        for triple in triples_to_check:
            critical_cell = self.__has_critical_cell(triple, kind_of_player)
            new_critical_cells += critical_cell

        if kind_of_player == AI.AI_SIGN:
            self.AI_critical_cells += new_critical_cells
        else:
            self.player_critical_cells += new_critical_cells

    def __has_critical_cell(self, triple, kind_of_player):
        signs = list(map(lambda x: self.players_board[x[0]][x[1]], triple))
        if signs.count(kind_of_player) == 2:
            critical_cell = list(filter(lambda x:
                                        self.potential_board[x[0]][x[1]] !=
                                        AI.USED_CELL, triple))
            return critical_cell
        return []

    def __check_free(self, row, col):
        return self.players_board[row][col] == AI.EMPTY_CELL

    def __update_players_board(self, row, col, sign):
        self.players_board[row][col] = sign

    def __is_victory(self, row, col):
        if self.player_critical_cells is not None:
            return (row, col) in self.player_critical_cells
        return False

    def __update_potential_board(self, row, col):
        self.potential_board[row][col] = AI.USED_CELL

        update_cells = []

        row_cells = [(row, 0), (row, 1), (row, 2)]
        row_signs = list(map(lambda x: self.players_board[x[0]][x[1]],
                             row_cells))
        if row_signs.count(AI.PLAYER_SIGN) == 1:
            update_row_cells = list(filter(lambda x:
                                           self.potential_board[x[0]][x[1]] !=
                                           AI.USED_CELL, row_cells))
        update_cells += update_row_cells

        col_cells = [(0, col), (1, col), (2, col)]
        col_signs = list(map(lambda x: self.players_board[x[0]][x[1]],
                             col_cells))
        if col_signs.count(AI.PLAYER_SIGN) == 1:
            update_col_cells = list(filter(lambda x:
                                           self.potential_board[x[0]][x[1]] !=
                                           AI.USED_CELL, col_cells))
        update_cells += update_col_cells

        # yet checks for the diagonals need to be made
        #if row == col:
            #major_diagonal = [(0, 0), (1, 1), (2, 2)].remove((row, col))
            #major_diagonal_signs = list(map(lambda x:...

        for cell in update_cells:
            row = cell[0]
            col = cell[1]
            self.potential_board[row][col] -= 1

    def __str__(self):
        # a way to print self.players_board
        pass
