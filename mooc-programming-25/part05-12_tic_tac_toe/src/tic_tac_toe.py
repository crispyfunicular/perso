# Write your solution here

def play_turn(game_board: list, x: int, y: int, piece: str):
    okej = [0, 1, 2]
    if x not in okej or y not in okej:
        return False
    if game_board[y][x] != "":
        return False
    game_board[y][x] = piece
    return True


def main():
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    game_sure = [['', '', ''], ['', 'X', 'X'], ['', 'O', '']]
    print(play_turn(game_board, 2, 0, "X"))
    print(play_turn(game_sure, 3, 0, "X"))
    print(game_board)
    print(game_sure)


if __name__ == "__main__":
    main()
