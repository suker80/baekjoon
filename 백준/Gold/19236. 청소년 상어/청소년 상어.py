graph = [[0] * 4 for _ in range(4)]
sequence = [0] * 17
direction = [[0, 0], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

from copy import deepcopy
for i in range(4):

    lst = list(map(int, input().split()))

    for j in range(0, 8, 2):
        graph[i][j//2] = lst[j]
        sequence[lst[j]] = [lst[j+1],i, j//2]



def switcing(sequence,graph,shark_y,shark_x):
    for frm in range(1,17):
        if sequence[frm] ==0:continue
        d , y,x = sequence[frm]
        i= 1
        dy,dx = direction[d]
        ny,nx = y+dy,x+dx
        for i in range(1,9):
            if 0<=ny<4 and 0<=nx<4 and [ny,nx] != [shark_y,shark_x]:
                to = graph[ny][nx]
                if sequence[to] == 0:
                    sequence[frm] = [d,ny,nx]
                    graph[ny][nx] = frm
                    graph[y][x] = 0
                    break


                else:
                    t_d,t_y,t_x = sequence[to]
                    sequence[frm] = [d,t_y,t_x]
                    sequence[to] = [t_d,y,x]
                    graph[y][x] ,graph[ny][nx] = graph[ny][nx] , graph[y][x]
                    break


            else :
                d= d+ 1 if d+1 <= 8 else d+1 - 8
                dy, dx = direction[d]
                ny, nx = y + dy, x + dx
    return sequence , graph
count = 0
def solve(y,x,graph,sequence,cnt = 0 ):
    global count
    if graph[y][x] == 0 or graph[y][x] == - 1:
        count = max(count,cnt)
        return
    fish = graph[y][x]
    d = sequence[fish][0]

    cnt += fish
    sequence[fish] = 0
    graph[y][x] =0


    sequence,graph = switcing(sequence,graph,y,x)


    for i in range(1,4):


        dy,dx = direction[d][0] * i , direction[d][1] * i
        ny,nx = y+dy,x+dx
        if 0<=ny<4 and 0<=nx<4:
            temp_graph = deepcopy(graph)
            temp_sequence = deepcopy(sequence)

            solve(ny,nx,temp_graph,temp_sequence,cnt)
    count = max(count,cnt)
solve(0,0,graph,sequence)

print(count)
