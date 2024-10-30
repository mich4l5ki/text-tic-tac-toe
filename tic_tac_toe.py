import re

WELCOME_PROMPT = "HELLO AND WELCOME TO TIC-TAC-TOE 2-PLAYERS GAME!!!\n"
PLACE_SYMBOL_PROMPT = "PLACE YOUR SYMBOL (ex. A1): "
OKGREEN = '\033[92m'
WARNING = '\033[93m'
ENDC = '\033[0m'

class TicTacToe:
    """Class for managing Tic Tac Toe game"""

    def __init__(self):
        self.playing = True
        self.player_turn = 1
        self.rows = {"A": 0, "B": 1, "C": 2}
        self.cols = {"1": 0, "2": 1, "3": 2}
        self.board_fields: list[list[str]] = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


    @property
    def board(self) -> str:
        """Generate a string representation of the game board."""
        return f"""
                1    2   3
            A | {self.board_fields[0][0]} | {self.board_fields[0][1]} | {self.board_fields[0][2]} |
            B | {self.board_fields[1][0]} | {self.board_fields[1][1]} | {self.board_fields[1][2]} |
            C | {self.board_fields[2][0]} | {self.board_fields[2][1]} | {self.board_fields[2][2]} |
            """


    def print_game_board(self):
        """Print current game board"""
        print(self.board)


    def update_field(self, field: str, symbol: str):
        """Update specific field of board with player's symbol """
        row = self.rows.get(field[0])
        col = self.cols.get(field[1])
        self.board_fields[row][col] = symbol


    def check_for_winner(self):
        """Check the board for a winner and return the winning symbol if found."""
        winning = self._check_row_for_winner() or self._check_col_for_winner() or self._check_diagonals_for_winners()

        if winning:
            self.playing = False
            return winning

        self.player_turn += 1
        return None


    def _check_row_for_winner(self):
        """Check rows for wins"""
        for i in range(3):
            if self.board_fields[i][0] == self.board_fields[i][1] == self.board_fields[i][2] != " ":
                self._highlight_winning_board([(i, 0), (i, 1), (i, 2)])
                return self.board_fields[i][0]
        return None


    def _check_col_for_winner(self):
        """Check columns for wins"""
        for i in range(3):
            if self.board_fields[0][i] == self.board_fields[1][i] == self.board_fields[2][i] != " ":
                self._highlight_winning_board([(0, i), (1, i), (2, i)])
                return self.board_fields[0][i]
        return None


    def _check_diagonals_for_winners(self):
        """Check diagonals for wins"""
        if self.board_fields[0][0] == self.board_fields[1][1] == self.board_fields[2][2] != " ":
            self._highlight_winning_board([(0, 0), (1, 1), (2, 2)])
            return self.board_fields[0][0]
        if self.board_fields[0][2] == self.board_fields[1][1] == self.board_fields[2][0] != " ":
            self._highlight_winning_board([(0, 2), (1, 1), (2, 0)])
            return self.board_fields[0][2]
        return None


    def _highlight_winning_board(self, positions):
        """Apply a highlight to the winning fields"""
        for row, col in positions:
            self.board_fields[row][col] = f"{OKGREEN}{self.board_fields[row][col]}{ENDC}"


    def get_valid_input(self) -> str:
        """Prompt the user until a valid input is provided."""
        while True:
            placement = input(PLACE_SYMBOL_PROMPT)
            if re.match("^[ABC][123]$", placement):
                return placement
            print(WARNING + "Invalid input! Please enter a valid position (A1, B2, etc.)." + ENDC)


if __name__ == "__main__":
    game = TicTacToe()
    print(WELCOME_PROMPT)
    while game.playing:
        player_symbol = "O" if game.player_turn % 2 == 0 else "X"
        game.print_game_board()
        print(f"TURN OF PLAYER {player_symbol}\n")
        placement_input = game.get_valid_input()
        game.update_field(placement_input, player_symbol)
        winner = game.check_for_winner()
        if winner:
            game.print_game_board()
            print(f"CONGRATULATION PLAYER {winner} WON")
