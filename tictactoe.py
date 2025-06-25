class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Board:
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        self.board_array = [[" "]*3 for _ in range(3)]
        self.turn = "X"

    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        col = move_index % 3
        if self.board_array[row][col] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][col] = self.turn
        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):
        for line in self.board_array + list(map(list, zip(*self.board_array))) + [[self.board_array[i][i] for i in range(3)], [self.board_array[i][2-i] for i in range(3)]]:
            if line[0] != " " and line.count(line[0]) == 3:
                return True, f"{line[0]} wins!"
        if all(cell != " " for row in self.board_array for cell in row):
            return True, "Cat's Game."
        return False, f"{self.turn}'s turn."

if __name__ == "__main__":
    board = Board()
    print("Welcome to Tic-Tac-Toe!")
    while True:
        print(board)
        try:
            move = input(f"{board.turn}'s move: ")
            board.move(move)
        except TictactoeException as e:
            print("Error:", e.message)
            continue
        game_over, message = board.whats_next()
        if game_over:
            print(board)
            print(message)
            break
