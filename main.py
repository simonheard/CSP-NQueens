def read_board_from_file(filename):
    with open(filename, 'r') as file:
        board = [int(line.strip()) for line in file if not line.startswith('#')]
        board = [x - 1 for x in board]
        board2d = [[0 for _ in range(len(board))] for _ in range(len(board))]
        for i in range(len(board)):
            board2d[i][board[i]] = 1
    return board2d

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print (board[i][j],end=' ')
        print()

def main():
    board = read_board_from_file('board1.txt')
    print_board(board)

if __name__ == '__main__':
    main()
