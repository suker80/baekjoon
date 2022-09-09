n, m = map(int, input().split())

robot_y, robot_x, cur_dir = map(int, input().split())

cell = [list(map(int,input().split())) for _ in range(n)]

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  ### 북 동 남 서
import sys

count = 0

sys.setrecursionlimit(10000)
def clean_machine(y, x, cur_dir):
    ############# 1번 ############
    global count
    if cell[y][x] == 0:
        cell[y][x] = 2
        count += 1
        ############ 2번 #############

    left_dir = cur_dir -1 if cur_dir >0 else 3

    ny, nx = y + direction[left_dir][0], x + direction[left_dir][1]

    back_dir = cur_dir +2 if cur_dir <2  else cur_dir - 2

    back_y, back_x = y + direction[back_dir][0], x + direction[back_dir][1]

    if cell[y - 1][x] and cell[y + 1][x] and cell[y][x - 1] and cell[y][x + 1] and cell[back_y][back_x] == 1:
        print(count)
        sys.exit()
    elif cell[y - 1][x] and cell[y + 1][x] and cell[y][x - 1] and cell[y][x + 1]:
        clean_machine(back_y, back_x, cur_dir)

    if cell[ny][nx] == 0:
        clean_machine(ny, nx, left_dir)
    elif cell[ny][nx] != 0:
        clean_machine(y, x, left_dir)


clean_machine(robot_y, robot_x, cur_dir)