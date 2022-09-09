
board = [list(map(str,input().split())) for _ in range(3)]

from collections import defaultdict,deque

visit = defaultdict(int)
x= [-1,1]
y = [-3,3]
board = [j for i in board for j in i]
for i,v in enumerate(board):
    if v == '0':
        zero_pos = i
def convert(number, n=9):
    number= int(number)
    answer = ''
    while number // n >= 1:
        remain = number % n
        number = number // n
        answer = str(remain) + answer
        if number < n:
            answer = str(number) + answer
    return int(answer)

board = ''.join(board)
queue = deque([[board,zero_pos,0]])
visit[int(board)] = 1
def swap(board,to,frm):

    board[to] ,board[frm] = board[frm],board[to]
    return ''.join(map(str,board))

def solve():
    while queue:
        board , zero_pos,count = queue.popleft()

        can_move = []
        if board == '123456780':
            print(count)
            return


        for x_pos in x:
            if zero_pos // 3  == (zero_pos+x_pos)//3 :
                can_move.append(zero_pos+x_pos)
        for y_pos in y:
            if 0<=zero_pos + y_pos < 9:
                can_move.append(zero_pos + y_pos)
        board_list = list(map(str,board))
        for can in can_move:
            temp_board = swap(board_list[:],zero_pos,can)

            if visit[int(temp_board)] == 0:
                queue.append([temp_board,can,count+1])
                visit[int(temp_board)] = 1
    print(-1)
solve()