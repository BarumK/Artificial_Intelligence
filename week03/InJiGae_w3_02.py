game_board = [' ', ' ', ' ',                                               # 게임보드 초기화
              ' ', ' ', ' ',
              ' ', ' ', ' ']

def empty_cells(board):                                                 # 비어있는 셀 찾기
    cells = []
    for x, cell in enumerate(board):                                    # 각각의 보드들의 순서에서 x(순서)와 셀(해당 순서의 값)을 뽑아냄
        if cell == ' ':                                                 # 셀이 비어있다면
            cells.append(x)                                             # 셀에다가 x를 append해줌
    return cells

def valid_move(x):                                                      # 비어있는 칸에 놓기
    return x in empty_cells(game_board)

def move(x, player):                                                    # x 위치에 놓기
    if valid_move(x):
        game_board[x] = player
        return True
    return False

def draw(board):
    for i, cell in enumerate(board):
        if i % 3 == 0:
            print("\n---------------")
        print("|", cell, "|", end='')
    print("\n---------------")

def evaluate(board):                                                    # 평가함수
    if check_win(board, 'X'):
        score = 1
    elif check_win(board, 'O'):
        score = -1
    else:
        score = 0
    return score

def check_win(board, player):                                           # 승리했는지 확인
    win_conf = [                                                        # 이기는 경우의 수
        [board[0], board[1], board[2]],                                 # 1행 모두 차지
        [board[3], board[4], board[5]],                                 # 2행 모두 차지
        [board[6], board[7], board[8]],                                 # 3행 모두 차지
        [board[0], board[3], board[6]],                                 # 1열 모두 차지
        [board[1], board[4], board[7]],                                 # 2열 모두 차지
        [board[2], board[5], board[8]],                                 # 3열 모두 차지
        [board[0], board[4], board[8]],                                 # 좌상 -> 우하 대각선 모두 차지
        [board[2], board[4], board[6]],                                 # 좌하 -> 우상 대각선 모두 차지
    ]
    return [player, player, player] in win_conf

def game_over(board):                                                   # 게임 끝났는지 판별
    return check_win(board, 'X') or check_win(board, 'O')

def minimax(board, depth, maxPlayer):
    pos = -1
    if depth == 0 or len(empty_cells(board)) == 0 or game_over(board):  # 게임이 종료되는 3가지 상황
        return -1, evaluate(board)

    if maxPlayer:
        value = -10000
        for p in empty_cells(board):
            board[p] = 'X'                                              # p의 위치에 놓고
            x, score = minimax(board, depth - 1, False)                 # x와 score를 가지고 미니맥스 값을 구함
            board[p] = ' '
            if score > value:
                value = score
                pos = p
    else:
        value = 10000
        for p in empty_cells(board):
            board[p] = 'O'
            x, score = minimax(board, depth - 1, True)
            board[p] = ' '
            if score < value:
                value = score
                pos = p

    return pos, value

if __name__ == "__main__":
    player = 'X'
    while True:
        draw(game_board)
        if len(empty_cells(game_board)) == 0 or game_over(game_board):
            break
        i, v = minimax(game_board, 9, player=='X')
        move(i, player)
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

    if check_win(game_board, 'X'):
        print("X 승리")
    elif check_win(game_board, 'O'):
        print("O 승리")
    else:
        print("무승부")