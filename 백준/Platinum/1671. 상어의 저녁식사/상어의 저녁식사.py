n = int(input())

graph = [[] for _ in range(n)]

shark = []

for i in range(n):
    shark.append(list(map(int, input().split())))

for i in range(n):

    size, speed, intel = shark[i]

    for j in range(n):
        if i == j:
            continue

        temp_size, temp_speed, temp_intel = shark[j]

        if size >= temp_size and speed >= temp_speed and intel >= temp_intel:
            if size == temp_size and speed == temp_speed and intel == temp_intel and i>= j :
                continue
            graph[i].append(j)
can_eat = [2] * n
matching = [-1] * n

'''

case 1 : 0,1 마리를 먹은상태 

case 2: 2마리를 먹은상태인데 다른 상어도 먹을 수 있다

case 3 : 상어가 서로를 먹을 때  




'''


# def dfs(node, move=False):
#     global answer
#
#     if visit[node]: return
#     visit[node] = True
#     is_eat = 0
#     for next_shark in graph[node]:
#
#         if matching[next_shark] == -1 or dfs(matching[next_shark]):
#
#             if can_eat[node] > 0:
#                 if matching[next_shark] == node or matching[node] == next_shark:
#                     continue
#                 can_eat[node] -= 1
#                 is_eat += 1
#                 matching[next_shark] = node
#             elif is_eat ==0:
#                 for i in range(n):
#                     if matching[i] == node:
#                         last_shark = i
#                         break
#
#                 matching[last_shark] = -1
#                 matching[next_shark] = node
#                 return True
#
#     return is_eat

def dfs(node):

    if visit[node] == 1: return

    visit[node] = 1


    for note in graph[node]:

        if matching[note] == -1 or dfs(matching[note]):
            matching[note] = node
            return True
    return False

answer =0
for i in range(n):
    for _ in range(2):
        visit = [False] * (n)
        if dfs(i):
            answer +=1

print(n-answer)