# 8-퍼즐의 너비 우선 탐색 코드
# 깊이 우선 탐색으로 하면 어떻게 될까? 한번 생각해보자
class State:
    def __init__(self, board, goal, moves=0):                           # 초기 board 생성
        self.board = board
        self.moves = moves
        self.goal = goal

    def get_new_board(self, i1, i2, moves):                             # 새로운 보드 생성: 연산자를 적용 시에 생성된 새로운 보드의 모양
        new_board = self.board[:]                                       # 일단 기존의 board를 가져와서
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]     # i1번째와 i2번째의 내용을 바꿈
        return State(new_board, self.goal, moves)                       # 그 후 리턴

    def expand(self, moves):                                            # 어느 방향으로 빈 칸이 이동되었는가?
        result = []
        i = self.board.index(0)
        if not i in [0, 1, 2]:                                          # 0의 위치가 0 1 2가 아니라면
            result.append(self.get_new_board(i, i - 3, moves))          # -> up 연산 수행해 확장
        if not i in [0, 3, 6]:                                          # 0의 위치가 0 3 6이 아니라면 
            result.append(self.get_new_board(i, i - 1, moves))          # -> left 연산 수행해 확장
        if not i in [2, 5, 8]:                                          # 0의 위치가 2 5 8이 아니라면 
            result.append(self.get_new_board(i, i + 1, moves))          # -> right 연산 수행해 확장
        if not i in [6, 7, 8]:                                          # 0의 위치가 6 7 8이 아니라면
            result.append(self.get_new_board(i, i + 3, moves))          # -> down 연산 수행해 확장
        return result

    def __str__(self):                                                  # board 출력
        return str(self.board[:3]) + "\n" + \
        str(self.board[3:6]) + "\n" + \
        str(self.board[6:]) + "\n" + \
        "____________________________"

    def __eq__(self, other):                                            # 새로 생성한 것이 이전과 같은지를 판단해줌
        return self.board == other.board


if __name__ == "__main__":
    puzzle = [1, 2, 3,
              0, 4, 6,
              7, 5, 8]                                                  # 초기 상태는 아무렇게나 해도 상관없음
    goal = [1, 2, 3,
            4, 5, 6,
            7, 8, 0]

    open_queue = []
    open_queue.append(State(puzzle, goal))

    closed_queue = []
    moves = 0

    while len(open_queue) != 0:                                         # open_queue가 빌 때까지 진행
        current = open_queue.pop(0)                                     # pop하면 맨 왼쪽 데이터를 꺼내는 것
        print(current)
        if current.board == goal:                                       # 목표와 같다면 멈춤
            print('탐색 성공')
            break

        moves = current.moves + 1                                       # 이동 횟수 증가
        closed_queue.append(current)                                    # 이동한 후 자식 노드들을 queue에 넣음
        for state in current.expand(moves):                             
            if (state in closed_queue) or (state in open_queue):        # closed, open queue에 없는 동안만 진행
                continue
            else:
                open_queue.append(state)